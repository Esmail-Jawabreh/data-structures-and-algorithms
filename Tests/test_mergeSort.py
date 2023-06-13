import pytest
from CC.sorting.Merge.merge import mergeSort


def test_mergeSort():
    # Sorting the sample array
    arr = [8, 4, 23, 42, 16, 15]
    mergeSort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

    # Sorting the reverse-sorted array
    arr = [20, 18, 12, 8, 5, -2]
    mergeSort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

    # Sorting a Few uniques
    arr = [5, 12, 7, 5, 5, 7]
    mergeSort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

    # Sorting a nearly-sorted array
    arr = [2, 3, 5, 7, 13, 11]
    mergeSort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]

    # Sorting an empty array
    arr = []
    mergeSort(arr)
    assert arr == []

    # Sorting an array with a single element
    arr = [42]
    mergeSort(arr)
    assert arr == [42]
