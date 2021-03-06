import pytest
from tests import (data_dict, random_string, random_number, random_list,
                   random_dict)
from myassert import AllAssertions
from myassert.assertions import assert_not_equal


@pytest.mark.parametrize("test_input, expected",
                         [(data_dict['str'], random_string(3)),
                          (data_dict['int'], random_number(10, 100)),
                          (data_dict['list'], random_list(3)),
                          (data_dict['dict'], random_dict(2)),
                          ])
def test_non_equal_values_pass(test_input, expected):
    assert_not_equal(test_input, expected)


@pytest.mark.parametrize("test_input, expected",
                         [(data_dict['str'], data_dict['str']),
                          (data_dict['int'], data_dict['int']),
                          (data_dict['list'], data_dict['list']),
                          (data_dict['dict'], data_dict['dict']),
                          ])
def test_equal_values_raise_error(test_input, expected):
    """
    Tests that matching values do not raise any error.
    :param test_input:
    :param expected:
    :return:
    """
    with pytest.raises(AssertionError):
        assert_not_equal(test_input, expected)


def test_call_from_class_passes():
    AllAssertions.assert_not_equal(data_dict['str'], data_dict['int'])


def test_call_from_class_fails():
    with pytest.raises(AssertionError):
        AllAssertions.assert_not_equal(data_dict['str'], data_dict['str'])
