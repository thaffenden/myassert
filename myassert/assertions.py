"""
Assertion statements.
"""
from pprint import pformat
from inspect import currentframe
from .error_messages import (error_message, equal_errors,
                             member_in_container_check)


def __raise_error(msg, pretty_print, error_msg, error_type):
    """
    Raise the error message using either a combination of of the custom error
    text, or the custom and the default error text.
    :param msg:
    :param pretty_print: Option to pretty print the message text.
    :param error_msg:
    :param error_type:
    :return:
    """
    if msg:
        if pretty_print is True:
            msg = pformat(msg, indent=2, width=79)
        raise_msg = error_message(msg="{}\n{}".format(msg, error_msg),
                                  error_type=error_type)
    else:
        raise_msg = error_message(error_msg, error_type)
    raise AssertionError(raise_msg)


def assert_true(value, msg="", pretty_print=True):
    """
    Raise an error if the value is anything other than True.
    :param value:
    :param msg:
    :param pretty_print:
    :return:
    """
    if value is not True:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg="'{}' is not True. Type: {}".format(value, type(value)))


def assert_false(value, msg="", pretty_print=True):
    """
    Raise an error if the value is anything other than False.
    :param value:
    :param msg:
    :param pretty_print:
    :return:
    """
    if value is not False:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg="'{}' is not False. Type: {}".format(value, type(value)))


def assert_none(value, msg="", pretty_print=True):
    """
    Raise an error if the value is anything other than None.
    :param value:
    :param msg:
    :param pretty_print:
    :return:
    """
    if value is not None:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg="'{}' is not None. Type: {}".format(value, type(value)))


def assert_not_none(value, msg="", pretty_print=True):
    """
    Raise an error if the value is None.
    :param value:
    :param msg:
    :param pretty_print:
    :return:
    """
    if value is None:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg="'{}' is None. Type: {}".format(value, type(value)))


def assert_equal(value, expected, msg="", pretty_print=True):
    """
    Check that two values are equal to each other.
    :param value:
    :param expected:
    :param msg:
    :param pretty_print:
    :return:
    """
    if value != expected:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg=equal_errors(value, expected))


def assert_not_equal(value, expected, msg="", pretty_print=True):
    """
    Assert that the values are not the same.
    :param value:
    :param expected:
    :param msg:
    :param pretty_print:
    :return:
    """
    if value == expected:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg=equal_errors(value, expected))


def assert_in(member, container, msg="", pretty_print=True):
    """
    Assert that a value is in another value. This can be text in a string, key
    in a dictionary, or item in a list.
    :param member:
    :param container:
    :param msg:
    :param pretty_print:
    :return:
    """
    if member not in container:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg=member_in_container_check(member, container,
                                                "does not exist"))


def assert_not_in(member, container, msg="", pretty_print=True):
    """
    Verify that item 'member' does not exist in 'container'.
    :param member:
    :param container:
    :param msg:
    :param pretty_print:
    :return:
    """
    if member in container:
        this_func = currentframe().f_code.co_name
        __raise_error(
            msg, pretty_print, error_type=this_func,
            error_msg=member_in_container_check(member, container, "exists"))
