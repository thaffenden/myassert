import pytest
from tests import random_string, random_list, random_dict
from myassert import AllAssertions
from myassert.assertions import assert_not_in

full_string = random_string(length=20)
sample_list = random_list()
sample_dict = random_dict()
sample_dict[full_string] = full_string


@pytest.mark.parametrize('member, container',
                         [(full_string[:3], full_string),
                          (sample_list[1], sample_list),
                          (full_string, sample_dict)])
def test_member_in_container_raises_error(member, container):
    with pytest.raises(AssertionError):
        assert_not_in(member, container)


@pytest.mark.parametrize('member, container',
                         [('not in here', 'This dummy text string'),
                          (500, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                          ("nope", {"one": 1, "two": 2, "three": 3})])
def test_member_not_in_container_passes(member, container):
    assert_not_in(member, container)


def test_call_from_class_passes():
    AllAssertions.assert_not_in("this", "in my really long string")


def test_call_from_class_fails():
    with pytest.raises(AssertionError):
        AllAssertions.assert_not_in("this", "this is in this string")
