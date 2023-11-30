#!/usr/bin/python3
"""A peak finding function"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using a binary search.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        A peak in the list of integers.
    """

    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
