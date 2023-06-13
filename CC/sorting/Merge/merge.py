def mergeSort(arr):
    """
    Sorts the given array using the Merge Sort algorithm.

    Args:
        arr (list).

    Returns:
        None. The array is sorted in-place.

    """
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        merge(left, right, arr)


def merge(left, right, arr):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left (list): The left subarray.
        right (list): The right subarray.
        arr (list): The array to store the merged result.

    Returns:
        None. The merged result is stored in the arr parameter.

    """
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
