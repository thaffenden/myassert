"""
Functions to format the error messages raised by the assertion statements.
"""

from difflib import ndiff
from pprint import pformat
from textwrap import wrap
from collections import OrderedDict


def error_message(msg, error_type):
    """
    Creates the basic error message format inside a block to make it as clear
    as possible on the output.
    :param msg:
    :param error_type:
    :return:
    """
    return '\n{err_type}\n{a}\n{b}\n{a}\n'.format(
        a='=' * 79, b=msg, err_type=_format_error_type(error_type))


def _format_error_type(error_type):
    """
    Format the text to print at the top of the assertion block.
    :param error_type: The assertion function name.
    :return:
    """
    return '{} failed:'.format(error_type.replace("_", " ")).upper()


def _format_comparison_values(value, expected):
    """
    Format the values for the comparison output, so the error message can
    display a neat, consistent output format.
    :param value:
    :param expected:
    :return:
    """
    value_length = len(str(value))
    expected_length = len(str(expected))

    if value_length + expected_length + 4 > 79:
        # If values over 79 characters long, wrap them to fit in block.
        if value_length > 79:
            value = str(wrap(str(value), width=79))

        if expected_length > 79:
            expected = str(wrap(str(expected), width=79))

        # Trim strings if too long for three lines
        if value_length > 237:
            value = '{}...'.format(str(value)[:234])

        if expected_length > 237:
            expected = '{}...'.format(str(expected)[:234])

    return {'value_string': value, 'expected_string': expected,
            'value_length': value_length, 'expected_length': expected_length}


def _values_are_not_equal_comparison_error(value, expected):
    """
    Value comparison error if the two values should be equal, but are not.
    :param value:
    :param expected:
    :return:
    """
    error_details = _format_comparison_values(value, expected)

    if (error_details['value_length']
            + error_details['expected_length']
            + 4) > 79:
        return '{}\n!=\n{}\n'.format(error_details['value_string'],
                                     error_details['expected_string'])
    else:
        return '{} != {}\n'.format(value, expected)


def _values_are_equal_comparison_error(value, expected):
    """
    Value comparison message if the two values are equal but should not be.
    :param value:
    :param expected:
    :return:
    """
    error_details = _format_comparison_values(value, expected)

    if (error_details['value_length']
            + error_details['expected_length']
            + 4) > 79:
        return '{}\nis equal to\n{}'.format(value, expected)
    else:
        return '{} is equal to {}'.format(value, expected)


# Type check errors
# Functions to format the specific type check errors, so appropriate messages
# can be generated based on the actual values passed.


def _type_checker(value, expected):
    """
    Check the data types are the same and append to error message warning if
    they are not.
    :param value:
    :param expected:
    :return:
    """
    value_type = type(value)
    expected_type = type(expected)
    if value_type != expected_type:
        return str('\n!!! Inputs are different data types !!!\n'
                   'value: {}\nexpected: {}'.format(value_type, expected_type))
    return False


def _string_comparison(value, expected):
    """
    Generate the diff for a string.
    :param value:
    :param expected:
    :return:
    """
    return '\n'.join(ndiff([value], [expected]))


def _dict_comparison(value, expected):
    """
    Generate the diff for a dict.
    :param value:
    :param expected:
    :return:
    """
    sorted_value = OrderedDict(sorted(value.items()))
    sorted_expected = OrderedDict(sorted(expected.items()))
    return '\n'.join(ndiff(sorted_value.items(), sorted_expected.items()))


def _list_comparison(value, expected):
    """
    Generate the diff for a list.
    :param value:
    :param expected:
    :return:
    """
    return '\n'.join(ndiff(pformat(value).splitlines(),
                           pformat(expected).splitlines()))


def _generate_error_with_diff(value, expected):
    """
    Format the error message for the 'assert_equal' and 'assert_not_equal'
    functions.
    :param value:
    :param expected:
    :return:
    """
    different_types = _type_checker(value, expected)

    if different_types:
        return different_types
    else:
        if isinstance(value, str):
            return _string_comparison(value, expected)

        if isinstance(value, int):
            return ""

        count_string = str('\nvalue contains {} items\nexpected contains {} '
                           'items'.format(len(value), len(expected)))

        if isinstance(value, dict):
            type_diff = '\nDIFF:\n{}'.format(_dict_comparison(value, expected))
            return '{}\n{}'.format(count_string, type_diff)

        if isinstance(value, list):
            type_diff = '\nDIFF:\n{}'.format(_list_comparison(value, expected))
            return '{}\n{}'.format(count_string, type_diff)


def equal_errors(value, expected):
    """
    Assemble the correct error message.
    :param value:
    :param expected:
    :return:
    """
    if value == expected:
        return _values_are_equal_comparison_error(value, expected)
    else:
        full_error = _values_are_not_equal_comparison_error(value, expected)
        full_error += _generate_error_with_diff(value, expected)
        return full_error


def member_in_container_check(member, container, error_type):
    """
    Message generator if a member does not exist in a container.
    The argument error type will always be 'does not exist', or 'exists'.
    :param member:
    :param container:
    :param error_type:
    :return:
    """
    error_details = _format_comparison_values(member, container)
    if isinstance(container, dict):
        member_item = 'Key'
    elif isinstance(container, list):
        member_item = 'List item'
    else:
        member_item = 'String'

    return str("{} '{}' {} in the {}:\n{}".format(
        member_item, member, error_type, type(container).__name__,
        error_details['expected_string'])
    )
