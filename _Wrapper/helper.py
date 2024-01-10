import inspect
import logging
import time
import math
import sys
from OrangeHRMData.Constants import Constants
from _Wrapper.logger import logger_adapter


# expects a func that takes a timeout and returns a boolean of success
# does not throw an assert error if the func test fails


def exists(func, **args) -> bool:
    loop_wait = .05
    timeout = Constants.default_throttle
    params = dict()
    for key, val in args.items():
        if str(key) == "timeout":
            if val is not None:
                timeout = int(val)
        elif str(key) == 'loop_wait':
            loop_wait = val
        elif str(key) == 'fail_message':
            continue
        else:
            params[key] = val

    first_attempt = True
    found = False
    start_time = time.time()

    while not found and (time.time() - start_time <= timeout or first_attempt):
        # simulate a do-while loop. This is to prevent possible false negatives if the timeout is 0
        first_attempt = False
        if len(params) > 0:
            found = func(**params)
        else:
            found = func()

        if not found:
            time.sleep(loop_wait)

    return found


# same as exists but throws an actual assert error if not found
def verify(func, **args) -> bool:
    if 'fail_message' in args:
        assert_message = args['fail_message']
    else:
        assert_message = 'No assert message given.'

    result = exists(func, **args)

    if hasattr(assert_message, '__call__'):
        assert result is True, assert_message()
    else:
        assert result is True, assert_message

    return result


def verify_comparison(expected, actual, fail_message=None):
    """
    Uses verify to perform a straight comparison. Actual can take a function signature or string value.
    This function will also format the fail message.
    :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
    :param actual: If this is an instance method, pass this in as a signature (ie, no parenthesis).
    :param fail_message: Message to send to console on failure
    :return:
    """
    if inspect.ismethod(actual):
        verify(lambda: actual() == expected, fail_message=get_formatted_fail_message(expected, actual(), fail_message))
    else:
        verify(lambda: actual == expected, fail_message=get_formatted_fail_message(expected, actual, fail_message))


def get_formatted_fail_message(expected, actual, error_message=None):
    if error_message is None:
        error_message = 'The actual value does not match the expected value.'
    return "{0}\nExpected: '{1}'\nActual: '{2}'".format(error_message, expected, actual)


def assert_equals_with_message(expected_value, actual_value,
                               error_message="The actual value does not match the expected value."):
    """
    Asserts if two values are equal. If they are not, outputs a message displaying both values.
    :param expected_value: Expected value
    :param actual_value: Actual value
    :param error_message: Message to send to console on failure
    """

    assert actual_value == expected_value, get_formatted_fail_message(expected_value, actual_value, error_message)


def verify_horizontal_vertical_order(element_array):
    """
    Verify the horizontal and vertical order of a "grid" array passed in
    :param element_array: Accepts a two-dimensional array with the horizontal/vertical position of elements to verify
                          Each row in the array corresponds to a SPECIFIC Y position, so any offset
                          elements will need their own row
    :return: None
    """

    # loop through each row. First verify the horizontal order of that row
    prev_row_y = -1
    for row_index, row in enumerate(element_array):
        cur_row_y = None
        prev_col_x = -1
        for col_index, col in enumerate(row):
            # verify all elements in the row have the same Y position
            if cur_row_y is not None:
                assert math.floor(col.get_element_location()['y']) == cur_row_y, \
                    "Row {0}, Col {1} not at same Y height".format(row_index, col_index)

            cur_row_y = math.floor(col.get_element_location()['y'])
            # verify the row's Y position is in the correct order
            assert math.floor(col.get_element_location()['y']) > prev_row_y

            # verify all columns in the row are in the correct order
            assert math.floor(col.get_element_location()['x']) > prev_col_x, \
                "Row {0}, Col {1} incorrect X position".format(row_index, col_index)
            prev_col_x = math.floor(col.get_element_location()['x'])

        prev_row_y = cur_row_y


# delayed assert/soft failure
def expect(expr, **args):
    if 'fail_message' in args:
        expect_message = "Failure: {0}".format(args['fail_message'])
    else:
        expect_message = "Failure: No expect message given"

    if 'take_screenshot' in args:
        bool_take_screenshot = args['take_screenshot']
    else:
        bool_take_screenshot = True

    if "timeout" in args:
        timeout = args['timeout']
    else:
        timeout = None

    result = exists(expr, timeout=timeout)

    if result is not True:
        # Assuming logger_adapter is an instance of LoggerAdapter
        logger_adapter.log(logging.INFO, msg=expect_message, log_take_screenshot=bool_take_screenshot)
    return result


def expect_comparison(expected, actual, fail_message=None, screenshot=True, timeout=None):
    """
    Uses expect to perform a straight comparison. Actual can take a function signature or string value.
    This function will also format the fail message.
    :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
    :param actual: If this is a instance method, pass this in as a signature (ie, no parenthesis).
    :param fail_message: str
    :param screenshot: bool
    :return:
    """

    def actual_value(actual):
        return actual() if inspect.ismethod(actual) else actual

    expect(lambda: actual_value(actual) == expected,
           fail_message=get_formatted_fail_message(expected, actual_value(actual), fail_message),
           take_screenshot=screenshot, timeout=timeout)


def add_text_to_clipboard(text):
    if sys.platform == 'win32':
        import win32clipboard

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()


def empty_lines_formatter(string):
    # When we get notes from new editor, every empty line returns extra \n (2 instead of 1).
    # We use this function to format notes returned from React notes editor.
    formatted_string = ''
    n_count = 0

    for i, s in enumerate(string):
        next_el_ind = i + 1
        if s == '\n':
            n_count += 1
            if (next_el_ind < len(string)) and (string[next_el_ind] == '\n'):
                pass
            else:
                # remove extra /n
                extra_chars = n_count // 2
                formatted_string += '\n' * (n_count - extra_chars)
                n_count = 0
        else:
            formatted_string += s

    return formatted_string
