"""
Testing the assert true function.
"""
import pytest
from myassert import AllAssertions
from myassert.assertions import assert_false


def test_false_passes():
    assert_false(False)


def test_true_raises_error():
    with pytest.raises(AssertionError):
        assert_false(True)


def test_function_that_returns_false_passes():
    def return_false():
        return False
    assert_false(return_false())


def test_function_that_returns_true_raises_error():
    def return_true():
        return True
    with pytest.raises(AssertionError):
        assert_false(return_true())


def test_call_from_class_passes():
    AllAssertions.assert_false(False)
