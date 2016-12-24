"""
Tests to cover the message format generator functions in the error messages
file.
"""
import pytest
from inspect import currentframe

from tests import random_string, random_list, random_dict
from myassert.error_messages import (error_message, _format_comparison_values)
from myassert.assertions import assert_equal


def test_base_error_message_format():
    msg_string = random_string()
    this_func = currentframe().f_code.co_name
    generated_error = error_message(msg=msg_string, error_type=this_func)
    assert generated_error == str('\nTEST BASE ERROR MESSAGE FORMAT FAILED:'
                                  '\n{a}\n{b}'
                                  '\n{a}\n'.format(a='=' * 79, b=msg_string))


@pytest.mark.parametrize(
    'value, expected',
    [(random_string(), random_string()),
     (random_string(length=79), random_string()),
     (random_string(), random_string(length=79)),
     (random_string(length=300), random_string(length=300)),
     (random_string(length=300), random_string()),
     (random_string(), random_string(length=300)),
     (random_list(length=100), random_list(length=100)),
     (random_list(length=100), random_list()),
     (random_list(), random_list(length=100)),
     (random_dict(), random_dict()),
     (random_dict(length=100), random_dict(length=100)),
     (random_dict(length=100), random_dict()),
     (random_dict(), random_dict(length=100))
     ])
def test_format_comparison_errors(value, expected):
    comparison = _format_comparison_values(value, expected)
    assert comparison["value_length"] == len(str(value))
    assert comparison["expected_length"] == len(str(expected))
