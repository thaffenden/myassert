"""
Assertion statements.
"""
from error_messages import (error_message, equal_errors,
                            member_in_container_check)


def __raise_error(msg, error_msg):
    """
    Raise the error message using either a combination of of the custom error
    text, or the custom and the default error text.
    :param msg:
    :param error_msg:
    :return:
    """
    if msg:
        raise_msg = error_message(msg="{}\n{}".format(msg, error_msg))
    else:
        raise_msg = error_message(error_msg)
    raise AssertionError(raise_msg)


def assert_true(value, msg=""):
    """
    Raise an error if the value is anything other than True.
    :param value:
    :param msg:
    :return:
    """
    if value is not True:
        __raise_error(msg, error_msg="'{}' is not True. Type: {}".format(
            value, type(value)))


def assert_false(value, msg=""):
    """
    Raise an error if the value is anything other than False.
    :param value:
    :param msg:
    :return:
    """
    if value is not False:
        __raise_error(msg, error_msg="'{}' is not False. Type: {}".format(
            value, type(value)))


def assert_none(value, msg=""):
    """
    Raise an error if the value is anything other than None.
    :param value:
    :param msg:
    :return:
    """
    if value is not None:
        __raise_error(msg, error_msg="'{}' is not None. Type: {}".format(
            value, type(value)))


def assert_not_none(value, msg=""):
    """
    Raise an error if the value is None.
    :param value:
    :param msg:
    :return:
    """
    if value is None:
        __raise_error(msg, error_msg="'{}' is None. Type: {}".format(
            value, type(value)))


def assert_equal(value, expected, msg=""):
    """
    Check that two values are equal to each other.
    :param value:
    :param expected:
    :param msg:
    :return:
    """
    if value != expected:
        __raise_error(msg, error_msg=equal_errors(value, expected))


def assert_not_equal(value, expected, msg=""):
    """
    Assert that the values are not the same.
    :param value:
    :param expected:
    :param msg:
    :return:
    """
    if value == expected:
        __raise_error(msg, error_msg=equal_errors(value, expected))


def assert_in(member, container, msg=""):
    """
    Assert that a value is in another value. This can be text in a string, key
    in a dictionary, or item in a list.
    :param member:
    :param container:
    :param msg:
    :return:
    """
    if member not in container:
        __raise_error(msg, error_msg=member_in_container_check(
            member, container, "does not exist"))


def assert_not_in(member, container, msg=""):
    """
    Verify that item 'member' does not exist in 'container'.
    :param member:
    :param container:
    :param msg:
    :return:
    """
    if member in container:
        __raise_error(msg, error_msg=member_in_container_check(
            member, container, "exists"))
