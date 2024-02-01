import base64
import binascii
import math
import os
import random


class Utils(object):

    def __init__(self):
        self.__date = None

    @property
    def date(self):
        try:
            return self.__date
        except AttributeError:
            from BaseUtils import DateUtil
            self.__date = DateUtil
            return self.__date

    @staticmethod
    def unique_string(strlen=32):
        trunc = -1 if strlen % 2 != 0 else None
        return binascii.hexlify(os.urandom(int(math.ceil(float(strlen) / 2)))).decode('utf-8')[:trunc]

    @staticmethod
    def unique_number(num_len):
        """
        This function will return random number with the length you specified
        :param num_len: Number if digits
        :return: int
        """
        range_start = 10 ** (num_len - 1)
        range_end = (10 ** num_len) - 1
        return random.randint(range_start, range_end)

    @staticmethod
    def unique_password():
        """
        Password needs to meet these criteria:
        - 11 characters long
        - 6 unique characters
        - Less than 60 characters log
        """
        return '1h8324b8768hwuF!!'

    @staticmethod
    def unicode_string(strlen=24):
        import random
        # Python 2/3

        ranges = [
            (0x0020, 0x007F),
            (0x00A0, 0x074F),
            (0x0780, 0x07BF),
            (0x0900, 0x137F),
            (0x13A0, 0x197F),
            (0x19E0, 0x19FF),
            (0x1D00, 0x1D7F),
            (0x1E00, 0x2BFF),
            (0x2E80, 0x2FDF),
            (0x2FF0, 0x31BF),
            (0x31F0, 0x42FF),  # Goes to 0x9FF but eliminating so 99% isn't Chinese characters
            (0xA000, 0xA4CF),
            (0xAC00, 0xD7AF),
            (0xF900, 0xFE0F),
            (0xFE20, 0xFFFF),
        ]

        alphabet = [
            chr(code_point) for current_range in ranges
            for code_point in range(current_range[0], current_range[1] + 1)
        ]
        return ''.join(random.choice(alphabet) for _ in range(strlen))

    @staticmethod
    def number_value(val, dec_delimiter='.', rtype=float):
        if val == '':
            return val
        import re
        p = r'[^0-9{0}\-]'.format(dec_delimiter)
        r = re.sub(p, '', str(val))  # Remove everything except numbers and the locale's decimal delimiter
        clean = r.replace(dec_delimiter, '.')
        return rtype(float(clean))

    # Below change for mpx-5109, security vulnerability (xss) for HTML escape char < > ' &
    @staticmethod
    def html_escape_replace(string):
        html_escape_table = {"&": "&amp;",
                             # '"': "&quot;",
                             "'": "&apos;",
                             ">": "&gt;",
                             "<": "&lt;",
                             "\'": "&apos;"}
        for i in html_escape_table.keys():
            if i in string:
                string = string.replace(i, html_escape_table[i])
        return string

    @staticmethod
    def detect_encoding_cp_1252(string):
        """This function validates if URL string is having encoding chars of windows cp-1252 which is also can be
        used for ISO-8859-1
        Used chars Windows-1252 from https://www.w3schools.com/charsets/ref_html_ansi.asp """
        CharCP_1252 = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~' \
                      '€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’""•--˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬�\xad\xa0®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞ' \
                      'ßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ “”'
        all_chars_from_list = True
        for char in string:
            if char in CharCP_1252:
                pass
            else:
                all_chars_from_list = False
                break
        return all_chars_from_list

    @staticmethod
    def is_base64_string(encoded_str=""):
        '''
        This function will return True if the string is in Base64 encoded format
        :param encoded_str:
        :return: Bool value: True if string is base64 string
        '''
        try:
            decoded_str = base64.b64decode(encoded_str)
            en_decoded_str = base64.b64encode(decoded_str)
            # convert bytes to string for comparision
            return True if en_decoded_str.decode() == encoded_str else False
        except:
            return False

    @staticmethod
    def fake_text(strlen, prefix=None):
        text = Utils.unique_string(strlen=strlen)
        from OrangeHRMData.Constants import Constants
        if prefix is None and Constants.fake_text_prefix is not None:
            prefix = Constants.fake_text_prefix

        if prefix:
            return "{0}{1}".format(prefix, text[len(prefix):len(text) - 1])
        return text

    def round(self, value, precision=0):
        import decimal
        if not precision:
            precision = '0.{0}'.format('0' * precision)

        return float(decimal.Decimal(value).quantize(decimal.Decimal(precision), rounding=decimal.ROUND_HALF_UP))

    @staticmethod
    def action_retry(action, verification_action):
        for i in range(0, 3):
            action()
            if verification_action():
                break
