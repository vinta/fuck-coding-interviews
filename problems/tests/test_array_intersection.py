# coding: utf-8
from problems.array_intersection import intersection


def test_intersection():
    assert intersection([6, 0, 12, 10, 16], [3, 15, 18, 20, 15]) == []
    assert intersection([1, 5, 2, 12, 6], [13, 10, 9, 5, 8]) == [5]
    assert intersection([3], [15]) == []
    assert intersection([2, 16, 8, 9], [14, 15, 2, 20]) == [2]
    assert intersection([6, 0, 12, 10, 16], [3, 15, 18, 20, 15]) == []
    assert intersection([1, 5, 2, 12, 6], [13, 10, 9, 5, 8]) == [5]
    assert intersection([3], [15]) == []
    assert intersection([2, 16, 8, 9], [14, 15, 2, 20]) == [2]
