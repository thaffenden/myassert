import pytest
from myassert import AllAssertions
from myassert.assertions import assert_none


def test_none_passes():
    assert_none(None)


def test_string_raises_error():
    with pytest.raises(AssertionError):
        assert_none("None")


def test_int_raises_error():
    with pytest.raises(AssertionError):
        assert_none(123)


def test_call_from_class_passes():
    AllAssertions.assert_none(None)


def test_call_from_class_fails():
    with pytest.raises(AssertionError):
        AllAssertions.assert_none("None")
