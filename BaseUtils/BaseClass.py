import logging
import pytest
from OrangeHRMData.Constants import Constants
from OrangeHRMData.Strings import Strings


@pytest.mark.usefixtures("driver")
class BaseClass:
    @classmethod
    def setup(cls):
        cls.s = Strings()
        cls.const = Constants()
        cls.logger = logging.getLogger('automation')

    @classmethod
    def __get_helper(cls):
        try:
            return cls.__helper
        except AttributeError:
            from _Wrapper import helper
            cls.__helper = helper
            return cls.__helper

    @classmethod
    def expect(cls, expr, **args):
        return cls.__get_helper().expect(expr, **args)

    @classmethod
    def expect_comp(cls, exp, act, timeout=20, fail_message=None):
        return cls.__get_helper().expect_comparison(expected=exp, actual=act, timeout=timeout,
                                                    fail_message=fail_message)

    @classmethod
    def verify(cls, func, **args):
        return cls.__get_helper().verify(func=func, **args)

    @classmethod
    def verify_comparison(cls, exp, act, fail_message=None):
        return cls.__get_helper().verify_comparison(expected=exp, actual=act,
                                                    fail_message=fail_message)
