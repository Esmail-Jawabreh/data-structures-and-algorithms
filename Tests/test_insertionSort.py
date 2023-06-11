import pytest
from CC.insertionSort.insertion import insertion_sort

def test_insertion_sort():
    # Sample Array: [8, 4, 23, 42, 16, 15]
    assert insertion_sort([8, 4, 23, 42, 16, 15]) == [4, 8, 15, 16, 23, 42]

    # Reverse-sorted Array: [20, 18, 12, 8, 5, -2]
    assert insertion_sort([20, 18, 12, 8, 5, -2]) == [-2, 5, 8, 12, 18, 20]

    # Few Uniques Array: [5, 12, 7, 5, 5, 7]
    assert insertion_sort([5, 12, 7, 5, 5, 7]) == [5, 5, 5, 7, 7, 12]

    # Nearly-sorted Array: [2, 3, 5, 7, 13, 11]
    assert insertion_sort([2, 3, 5, 7, 13, 11]) == [2, 3, 5, 7, 11, 13]

