import pytest
from CC.Mock_Interviews.matrix_Sum.matrixSum import sum_rows


def test_one():
    actual = sum_rows([[1, 2, 3], [3, 5, 7], [1, 7, 10]])
    expected = 	[6, 15, 18]
    assert actual == expected


def test_two():
    actual = sum_rows([[0, 1, 5], [-4, 7, 2], [-3, 12, 11]])   
    expected = [6, 5, 20]
    assert actual == expected