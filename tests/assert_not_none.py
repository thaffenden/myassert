import pytest
from myassert import AllAssertions
from myassert.assertions import assert_not_none


def test_none_raises_error():
    with pytest.raises(AssertionError):
        assert_not_none(None)


def test_string_passes():
    assert_not_none("None")


def test_int_passes():
    assert_not_none(123)


def test_call_from_class_passes():
    AllAssertions.assert_not_none(True)


def test_call_from_class_fails():
    with pytest.raises(AssertionError):
        AllAssertions.assert_not_none(None)
