# Binary Search Implementation
# This code demonstrates two implementations of the binary search algorithm:
# 1. Iterative approach using a loop
# 2. Recursive approach

# Input array
# The array contains unsorted integers. Binary search requires the array to be sorted.
arr = [34, 55, 623, 344, 124, 1324, 533, 6565, 122, 345, 665, 12]


def binary_search_using_loop(arr: list, find_num):
    """
    Perform binary search iteratively to find the index of `find_num` in a sorted array.

    Steps:
    1. Sort the array to ensure binary search can be applied.
    2. Initialize two pointers, `left_index` and `right_index`, representing the search boundaries.
    3. Calculate the middle index and compare the middle element with the target (`find_num`).
    4. Narrow down the search range based on the comparison result.
    5. Repeat until the element is found or the range becomes invalid.

    :param arr: List of integers to search within
    :param find_num: Integer to find in the array
    :return: Index of `find_num` if found, otherwise -1
    """
    arr.sort()  # Sort the array before searching
    left_index, right_index = 0, len(arr) - 1  # Initialize search boundaries

    while left_index <= right_index:
        # Calculate the middle index using integer division
        mid_index = (left_index + right_index) // 2

        # Check if the middle element is the target
        if arr[mid_index] == find_num:
            return mid_index

        # If the middle element is smaller than the target, search the right half
        if arr[mid_index] < find_num:
            left_index = mid_index + 1
        # Otherwise, search the left half
        else:
            right_index = mid_index - 1

    # Return -1 if the target is not found in the array
    return -1


def binary_search_using_recursion(arr: list, find_num, left_index, right_index):
    """
    Perform binary search recursively to find the index of `find_num` in a sorted array.

    Steps:
    1. Base Case: If the search range is invalid (`right_index < left_index`), return -1.
    2. Calculate the middle index of the current search range.
    3. Compare the middle element with the target (`find_num`).
    4. If the middle element matches the target, return its index.
    5. Otherwise, recursively adjust the search range based on the comparison.

    :param arr: List of integers to search within
    :param find_num: Integer to find in the array
    :param left_index: Left boundary of the current search range
    :param right_index: Right boundary of the current search range
    :return: Index of `find_num` if found, otherwise -1
    """
    # Base case: If the range is invalid, the element is not present
    if right_index < left_index:
        return -1

    # Calculate the middle index using integer division
    mid_index = (left_index + right_index) // 2

    # Check if the middle element is the target
    if arr[mid_index] == find_num:
        return mid_index

    # If the middle element is smaller than the target, search the right half
    if arr[mid_index] < find_num:
        return binary_search_using_recursion(arr, find_num, mid_index + 1, right_index)
    # Otherwise, search the left half
    else:
        return binary_search_using_recursion(arr, find_num, left_index, mid_index - 1)


# Sort the array before performing binary search
# Sorting is essential because binary search assumes the input is sorted.
arr.sort()

# Example usage of the recursive binary search function
# We are searching for the number 6565 in the sorted array.
idx = binary_search_using_recursion(arr, 6565, 0, len(arr) - 1)
print(f"Element found at index: {idx}")  # Output the result, -1 if not found
