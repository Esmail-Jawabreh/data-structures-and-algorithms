import pytest
from CC.Mock_Interviews.fibonacci_Sequence.fibonacciSequence import fib_recursive, fib_iterative


def test_zero_fib():
    actual = fib_recursive(0) and fib_iterative(0)
    expected = 0
    assert actual == expected


def test_one_fib():
    actual = fib_recursive(1) and fib_iterative(1)
    expected = 1
    assert actual == expected


def test_two_fib():
    actual = fib_recursive(2) and fib_iterative(2)
    expected = 1
    assert actual == expected


def test_three_fib():
    actual = fib_recursive(3) and fib_iterative(3)
    expected = 2
    assert actual == expected


def test_four_fib():
    actual = fib_recursive(4) and fib_iterative(4)
    expected = 3
    assert actual == expected


def test_five_fib():
    actual = fib_recursive(5) and fib_iterative(5)
    expected = 5
    assert actual == expected


def test_six_fib():
    actual = fib_recursive(6) and fib_iterative(6)
    expected = 8
    assert actual == expected


def test_seven_fib():
    actual = fib_recursive(7) and fib_iterative(7)
    expected = 13
    assert actual == expected


def test_eight_fib():
    actual = fib_recursive(8) and fib_iterative(8)
    expected = 21
    assert actual == expected


def test_nine_fib():
    actual = fib_recursive(9) and fib_iterative(9)
    expected = 34
    assert actual == expected


def test_ten_fib():
    actual = fib_recursive(14) and fib_iterative(14)
    expected = 377
    assert actual == expected


def test_eleven_fib():
    actual = fib_iterative(45) #and fib_recursive(45)
    expected = 1134903170
    assert actual == expected
