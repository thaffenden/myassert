"""
Testing the assert true function.
"""
import pytest
from myassert import AllAssertions
from myassert.assertions import assert_true


def test_true_passes():
    assert_true(True)


def test_false_raises_error():
    with pytest.raises(AssertionError):
        assert_true(False)


def test_function_that_returns_true_passes():
    def return_true():
        return True
    assert_true(return_true())


def test_function_that_returns_false_raises_error():
    def return_false():
        return False
    with pytest.raises(AssertionError):
        assert_true(return_false())


def test_fail_with_custom_error():
    with pytest.raises(AssertionError):
        assert_true(False, "Custom error message")


def test_call_from_class_passes():
    AllAssertions.assert_true(True)


def test_call_from_class_fails():
    with pytest.raises(AssertionError):
        AllAssertions.assert_true(False)
