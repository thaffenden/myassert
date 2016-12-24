from .assertions import (assert_true, assert_false, assert_none,
                         assert_not_none, assert_equal, assert_not_equal,
                         assert_in, assert_not_in,)


class AllAssertions(object):
    """
    This class is intended as a wrapper, so it can be used as a superclass for
    another class to inherit from, allowing you to call your assertions in the
    format:
    self.assert_true(...)
    self.assert_equal(...)
    etc.
    """
    @staticmethod
    def assert_true(value, msg='', pretty_print=True):
        return assert_true(value, msg, pretty_print)

    @staticmethod
    def assert_false(value, msg='', pretty_print=True):
        return assert_false(value, msg, pretty_print)

    @staticmethod
    def assert_none(value, msg='', pretty_print=True):
        return assert_none(value, msg, pretty_print)

    @staticmethod
    def assert_not_none(value, msg='', pretty_print=True):
        return assert_not_none(value, msg, pretty_print)

    @staticmethod
    def assert_equal(value, expected, msg='', pretty_print=True):
        return assert_equal(value, expected, msg, pretty_print)

    @staticmethod
    def assert_not_equal(value, expected, msg='', pretty_print=True):
        return assert_not_equal(value, expected, msg, pretty_print)

    @staticmethod
    def assert_in(member, container, msg='', pretty_print=True):
        return assert_in(member, container, msg, pretty_print)

    @staticmethod
    def assert_not_in(member, container, msg='', pretty_print=True):
        return assert_not_in(member, container, msg, pretty_print)
