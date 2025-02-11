def shell_sort(arr):
    """
    Sorts the given list 'arr' using the Shell Sort algorithm.

    Shell Sort is an optimized version of insertion sort that works by
    comparing elements separated by a gap and reducing the gap over time.

    Parameters:
    arr (list): The list to be sorted.

    Time Complexity:
        - Best Case: O(n log n)  [When the list is nearly sorted]
        - Average Case: O(n^(3/2)) or O(n^(5/4)) (depends on gap sequence)
        - Worst Case: O(n^2)  [When using simple gap sequences like n/2, n/4,...]

    Space Complexity:
        - O(1) (In-place sorting, no extra space required)
    """
    size = len(arr)
    gap = size // 2  # Initial gap size

    # Gradually reduce the gap
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]  # Element to be compared
            j = i

            # Insertion sort with gap distance
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]  # Shift larger element forward
                j -= gap
            arr[j] = anchor  # Place the element at the correct position

        gap //= 2  # Reduce the gap size


if __name__ == "__main__":
    arr = [10, 3, 15, 7, 8, 23, 98, 29]  # Sample list
    shell_sort(arr)  # Sort the list
    print("Sorted Array:", arr)  # Print sorted result
