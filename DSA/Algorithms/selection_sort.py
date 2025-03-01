def selection_sort(arr):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.

    Time Complexity:
    - Best Case: O(n^2) (Even if the array is already sorted, it still compares all elements)
    - Average Case: O(n^2) (Two nested loops always iterate over the array)
    - Worst Case: O(n^2) (Fully reversed order requires maximum swaps)

    Space Complexity: O(1) (In-place sorting with no extra storage)

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    None: The input list is sorted in place.
    """
    size = len(arr)

    for i in range(size - 1):  # Iterate through each element except the last
        min_index = i  # Assume the current element is the smallest

        # Find the index of the smallest element in the remaining unsorted part
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the index of the new minimum element

        # Swap if a smaller element is found
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap values


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (
            [78, 12, 15, 8, 61, 53, 23, 27],
            [8, 12, 15, 23, 27, 53, 61, 78],
        ),  # Random order
        ([5, 3, 8, 6, 2, 7, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8]),  # Unsorted list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted list
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted list
        ([10], [10]),  # Single-element list
        ([], []),  # Empty list
    ]

    # Running tests
    for i, (input_list, expected) in enumerate(test_cases):
        selection_sort(input_list)  # Sort the list
        assert (
            input_list == expected
        ), f"Test case {i+1} failed: Expected {expected}, got {input_list}"
        print(f"Test case {i+1} passed")

    print("All test cases passed successfully!")
