def swap(a, b, arr):
    """
    Swaps the elements at indices `a` and `b` in the array `arr`.
    This operation is only performed if the indices are different to avoid unnecessary writes.
    """
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    """
    Partitions the array using the last element as the pivot.
    Elements smaller than or equal to the pivot are moved to the left,
    and elements greater than the pivot are moved to the right.

    Parameters:
    - elements: List of elements to be sorted.
    - start: Starting index of the partition.
    - end: Ending index of the partition (pivot index).

    Returns:
    - p_index: Final position of the pivot after partitioning.
    """
    pivot = elements[end]  # Choosing the last element as the pivot
    p_index = start  # Pointer for the smaller element

    for i in range(start, end):  # Iterate through the list (excluding the pivot)
        if elements[i] <= pivot:
            swap(i, p_index, elements)  # Move smaller element to the left partition
            p_index += 1  # Increment partition index

    swap(p_index, end, elements)  # Place pivot at its correct position
    return p_index  # Return pivot index for recursive sorting


def quick_sort(elements, start, end):
    """
    Implements the Quick Sort algorithm using recursion.

    Parameters:
    - elements: List of elements to be sorted.
    - start: Starting index of the sub-array to sort.
    - end: Ending index of the sub-array to sort.

    Quick Sort operates by partitioning the array and recursively sorting the left and right subarrays.
    """
    if start < end:
        pi = partition(elements, start, end)  # Partition the array
        quick_sort(elements, start, pi - 1)  # Recursively sort the left part
        quick_sort(elements, pi + 1, end)  # Recursively sort the right part


if __name__ == "__main__":
    elements = [11, 9, 8, 29, 7, 2, 33, 15, 28]  # Sample list
    quick_sort(elements, 0, len(elements) - 1)  # Perform Quick Sort
    print("Sorted array:", elements)  # Display sorted elements
