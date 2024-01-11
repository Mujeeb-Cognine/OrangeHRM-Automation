import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from OrangeHRMData.Enums import ActionKeys
from OrangeHRMData.Strings import Strings
import inspect
import logging
import time
import math
from OrangeHRMData.Constants import Constants
from _Wrapper.logger import logger_adapter


@pytest.mark.usefixtures("driver")
class BaseClass:
    driver = None  # Class variable to store the driver
    logger = logging.getLogger(__name__)

    @classmethod
    def set_driver(cls, driver: WebDriver):
        if not isinstance(driver, WebDriver):
            raise TypeError("Invalid driver type. Must be an instance of WebDriver.")
        cls.driver = driver
        cls.logger.info("Driver successfully set.")

    @classmethod
    def setup(cls):
        cls.s = Strings()
        cls.const = Constants()

    @classmethod
    def navigate_to_url(cls, url: str):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.get(url)
        cls.driver.maximize_window()

    @classmethod
    def find_element(cls, by, value):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_element(by, value)

    @classmethod
    def find_elements(cls, by, value):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.find_elements(by, value)

    @classmethod
    def click_element(cls, by, value):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        element = cls.find_element(by, value)
        element.click()

    @classmethod
    def send_keys_to_element(cls, by, value, keys):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        element = cls.find_element(by, value)
        element.send_keys(keys)

    @classmethod
    def wait_for_element(cls, by, value, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    @classmethod
    def go_back(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.back()

    @classmethod
    def go_forward(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.forward()

    @classmethod
    def refresh_page(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.refresh()

    @classmethod
    def take_screenshot(cls, filename):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.save_screenshot(filename)

    @classmethod
    def get_screenshot_as_base64(cls):
        return cls.driver.get_screenshot_as_base64()

    @classmethod
    def close_browser(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.close()

    @classmethod
    def quit_browser(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.quit()

    @classmethod
    def get_current_url(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.current_url

    @classmethod
    def get_page_title(cls):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return cls.driver.title

    @classmethod
    def implicitly_wait(cls, seconds):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        cls.driver.implicitly_wait(seconds)

    @classmethod
    def wait_for_element_clickable(cls, by, value, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    @classmethod
    def wait_for_visibility_of_element(cls, by, value, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    @classmethod
    def wait_for_invisibility_of_element(cls, by, value, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.invisibility_of_element_located((by, value))
        )

    @classmethod
    def wait_for_text_to_be_present_in_element(cls, by, value, text, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )

    @classmethod
    def clear_element(cls, by, value):
        element = cls.find_element(by, value)
        element.clear()

    @classmethod
    def get_text(cls, by, value):
        element = cls.find_element(by, value)
        return element.text

    @classmethod
    def get_attribute(cls, by, value, attribute_name):
        element = cls.find_element(by, value)
        return element.get_attribute(attribute_name)

    @classmethod
    def perform_hover(cls, by, value):
        element = cls.find_element(by, value)
        ActionChains(cls.driver).move_to_element(element).perform()

    @classmethod
    def press_key(cls, key):
        ActionChains(cls.driver).send_keys(key).perform()

    @classmethod
    def press_enter(cls):
        cls.press_key(ActionKeys.ENTER)

    @classmethod
    def press_tab(cls):
        cls.press_key(ActionKeys.TAB)

    @classmethod
    def switch_to_frame(cls, by, value):
        frame = cls.find_element(by, value)
        cls.driver.switch_to.frame(frame)

    @classmethod
    def switch_to_default_content(cls):
        cls.driver.switch_to.default_content()

    @classmethod
    def get_current_window_handle(cls):
        return cls.driver.current_window_handle

    @classmethod
    def accept_alert(cls):
        Alert(cls.driver).accept()

    @classmethod
    def dismiss_alert(cls):
        Alert(cls.driver).dismiss()

    @classmethod
    def get_alert_text(cls):
        return Alert(cls.driver).text

    @classmethod
    def select_dropdown_option_by_value(cls, by, value, option_value):
        element = cls.find_element(by, value)
        select = Select(element)
        select.select_by_value(option_value)

    @classmethod
    def select_dropdown_option_by_index(cls, by, value, index):
        element = cls.find_element(by, value)
        select = Select(element)
        select.select_by_index(index)

    @classmethod
    def select_dropdown_option_by_visible_text(cls, by, value, visible_text):
        element = cls.find_element(by, value)
        select = Select(element)
        select.select_by_visible_text(visible_text)

    @classmethod
    def execute_script(cls, script, *args):
        return cls.driver.execute_script(script, *args)

    @classmethod
    def execute_async_script(cls, script, *args):
        return cls.driver.execute_async_script(script, *args)

    @classmethod
    def get_cookies(cls):
        return cls.driver.get_cookies()

    @classmethod
    def add_cookie(cls, cookie_dict):
        cls.driver.add_cookie(cookie_dict)

    @classmethod
    def delete_cookie(cls, cookie_name):
        cls.driver.delete_cookie(cookie_name)

    @classmethod
    def delete_all_cookies(cls):
        cls.driver.delete_all_cookies()

    @classmethod
    def get_window_size(cls):
        return cls.driver.get_window_size()

    @classmethod
    def get_window_position(cls):
        return cls.driver.get_window_position()

    @classmethod
    def set_browser_size(cls, width, height):
        cls.driver.set_window_size(width, height)

    @classmethod
    def maximize_browser_window(cls):
        cls.driver.maximize_window()

    @classmethod
    def set_browser_position(cls, x, y):
        cls.driver.set_window_position(x, y)

    @classmethod
    def take_element_screenshot(cls, by, value, filename):
        element = cls.find_element(by, value)
        element.screenshot(filename)

    @classmethod
    def drag_and_drop(cls, source_by, source_value, target_by, target_value):
        source_element = cls.find_element(source_by, source_value)
        target_element = cls.find_element(target_by, target_value)
        ActionChains(cls.driver).drag_and_drop(source_element, target_element).perform()

    @classmethod
    def scroll_to_element(cls, by, value):
        element = cls.find_element(by, value)
        cls.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @classmethod
    def scroll_to_bottom(cls):
        cls.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @classmethod
    def switch_to_alert(cls):
        return cls.driver.switch_to.alert

    @classmethod
    def get_all_window_handles(cls):
        return cls.driver.window_handles

    @classmethod
    def wait_for_alert(cls, timeout=10):
        if not cls.driver:
            raise ValueError("Driver not initialized. Call set_driver() first.")
        return WebDriverWait(cls.driver, timeout).until(
            EC.alert_is_present()
        )

    @classmethod
    def verify_element_present(cls, by, value):
        try:
            cls.find_element(by, value)
            cls.logger.info(f"Element located by {by} with value {value} is present.")
            return True
        except:
            cls.logger.error(f"Element located by {by} with value {value} is not present.")
            return False

    @classmethod
    def verify_text_in_element(cls, by, value, expected_text):
        element = cls.find_element(by, value)
        actual_text = element.text
        try:
            assert expected_text == actual_text
            cls.logger.info(f"Text in element is as expected: {expected_text}")
            return True
        except AssertionError:
            cls.logger.error(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")
            return False

    @classmethod
    def verify_attribute_value(cls, by, value, attribute, expected_value):
        element = cls.find_element(by, value)
        actual_value = element.get_attribute(attribute)
        try:
            assert expected_value == actual_value
            cls.logger.info(f"Attribute '{attribute}' has the expected value: {expected_value}")
            return True
        except AssertionError:
            cls.logger.error(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")
            return False

    @classmethod
    def expect_element_present(cls, by, value):
        try:
            cls.find_element(by, value)
            cls.logger.info(f"Element located by {by} with value {value} is present.")
        except:
            cls.logger.error(f"Element located by {by} with value {value} is not present.")
            raise AssertionError(f"Element located by {by} with value {value} is not present.")

    @classmethod
    def expect_text_in_element(cls, by, value, expected_text):
        element = cls.find_element(by, value)
        actual_text = element.text
        try:
            assert expected_text == actual_text
            cls.logger.info(f"Text in element is as expected: {expected_text}")
        except AssertionError:
            cls.logger.error(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")
            raise AssertionError(f"Text in element doesn't match. Expected: {expected_text}, Actual: {actual_text}")

    @classmethod
    def expect_attribute_value(cls, by, value, attribute, expected_value):
        element = cls.find_element(by, value)
        actual_value = element.get_attribute(attribute)
        try:
            assert expected_value == actual_value
            cls.logger.info(f"Attribute '{attribute}' has the expected value: {expected_value}")
        except AssertionError:
            cls.logger.error(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")
            raise AssertionError(
                f"Attribute '{attribute}' value does not match. Expected: {expected_value}, Actual: {actual_value}")

    @classmethod
    def verify_equal(cls, actual, expected, message=None):
        try:
            assert actual == expected, message
            cls.logger.info(f"Verification passed: Actual value '{actual}' is equal to Expected value '{expected}'")
        except AssertionError as e:
            cls.logger.error(f"Verification failed: {str(e)}")
            return False
        return True

    @classmethod
    def verify_not_equal(cls, actual, not_expected, message=None):
        try:
            assert actual != not_expected, message
            cls.logger.info(
                f"Verification passed: Actual value '{actual}' is not equal to Not Expected value '{not_expected}'")
        except AssertionError as e:
            cls.logger.error(f"Verification failed: {str(e)}")
            return False
        return True

    @classmethod
    def expect_equal(cls, actual, expected, message=None):
        try:
            assert actual == expected, message
            cls.logger.info(f"Expectation passed: Actual value '{actual}' is equal to Expected value '{expected}'")
        except AssertionError as e:
            cls.logger.error(f"Expectation failed: {str(e)}")
            raise AssertionError(str(e))

    @classmethod
    def expect_not_equal(cls, actual, not_expected, message=None):
        try:
            assert actual != not_expected, message
            cls.logger.info(
                f"Expectation passed: Actual value '{actual}' is not equal to Not Expected value '{not_expected}'")
        except AssertionError as e:
            cls.logger.error(f"Expectation failed: {str(e)}")
            raise AssertionError(str(e))

    @classmethod
    def exists(cls, func, **args) -> bool:
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

    @classmethod
    def verify(cls, func, **args) -> bool:
        if 'fail_message' in args:
            assert_message = args['fail_message']
        else:
            assert_message = 'No assert message given.'

        result = cls.exists(func, **args)

        if hasattr(assert_message, '__call__'):
            assert result is True, assert_message
        else:
            assert result is True, assert_message

        return result

    @classmethod
    def verify_comparison(cls, expected, actual, fail_message=None):
        """
        Uses verify to perform a straight comparison. Actual can take a function signature or string value.
        This function will also format the fail message.
        :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
        :param actual: If this is an instance method, pass this in as a signature (ie, no parenthesis).
        :param fail_message: Message to send to console on failure
        :return:
        """
        if inspect.ismethod(actual):
            cls.verify(lambda: actual() == expected,
                       fail_message=cls.get_formatted_fail_message(expected, actual(), fail_message))
        else:
            cls.verify(lambda: actual == expected,
                       fail_message=cls.get_formatted_fail_message(expected, actual, fail_message))

    @classmethod
    def get_formatted_fail_message(cls, expected, actual, error_message=None):
        if error_message is None:
            error_message = 'The actual value does not match the expected value.'
        return "{0}\nExpected: '{1}'\nActual: '{2}'".format(error_message, expected, actual)

    @classmethod
    def assert_equals_with_message(cls, expected_value, actual_value,
                                   error_message="The actual value does not match the expected value."):
        """
        Asserts if two values are equal. If they are not, outputs a message displaying both values.
        :param expected_value: Expected value
        :param actual_value: Actual value
        :param error_message: Message to send to console on failure
        """

        assert actual_value == expected_value, (
            cls.get_formatted_fail_message(expected_value, actual_value, error_message))

    @classmethod
    def verify_horizontal_vertical_order(cls, element_array):
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

    @classmethod
    def expect(cls, expr, **args):
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

        result = cls.exists(expr, timeout=timeout)

        if result is not True:
            # Assuming logger_adapter is an instance of LoggerAdapter
            logger_adapter.log(logging.INFO, msg=expect_message, log_take_screenshot=bool_take_screenshot)
        return result

    @classmethod
    def expect_comparison(cls, expected, actual, fail_message=None, screenshot=True, timeout=None):
        """
        Uses expect to perform a straight comparison. Actual can take a function signature or string value.
        This function will also format the fail message.
        :param timeout:
        :param expected: A string, int, float, boolean, or iterable to serve as the expected value.
        :param actual: If this is a instance method, pass this in as a signature (ie, no parenthesis).
        :param fail_message: str
        :param screenshot: bool
        :return:
        """

        def actual_value():
            return actual() if inspect.ismethod(actual) else actual

        cls.expect(lambda: actual_value() == expected,
                   fail_message=cls.get_formatted_fail_message(expected, actual_value(), fail_message),
                   take_screenshot=screenshot, timeout=timeout)

    @classmethod
    def add_text_to_clipboard(cls, text):
        import win32clipboard

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
        win32clipboard.CloseClipboard()

    @classmethod
    def empty_lines_formatter(cls, string):
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
