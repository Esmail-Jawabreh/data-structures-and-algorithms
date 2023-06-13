def insertion_sort(arr):
    """
    Sorts a list of numbers in ascending order using the insertion sort algorithm.

    Args:
        arr (list).

    Returns:
        list: The sorted list.

    Example:
        insertion_sort([4, 2, 1, 3]) >>> [1, 2, 3, 4]
    """
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr
