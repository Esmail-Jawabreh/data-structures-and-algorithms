import pytest
from CC.arrayBinarySearch.arrayBinarySearch import binary_search


def test_one():
    actual = binary_search([4, 8, 15, 16, 23, 42], 15)
    expected = 2
    assert actual == expected


def test_two():
    actual = binary_search([-131, -82, 0, 27, 42, 68, 179], 42)
    expected = 4
    assert actual == expected


def test_three():
    actual = binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    expected = -1
    assert actual == expected


def test_four():
    actual = binary_search([1, 2, 3, 5, 6, 7], 4)
    expected = -1
    assert actual == expected
