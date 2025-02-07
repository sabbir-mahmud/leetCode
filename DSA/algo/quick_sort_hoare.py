def swap(a, b, arr):
    """
    Swaps the elements at indices `a` and `b` in the array `arr`.
    """
    arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    """
    Partitions the array using the first element as the pivot.
    Elements smaller than or equal to the pivot are moved to its left,
    and elements greater than the pivot are moved to its right.
    Returns the final index of the pivot after partitioning.
    """
    pivot_index = start  # Choosing the first element as the pivot
    pivot = elements[pivot_index]

    while start < end:
        # Move `start` forward if the current element is less than or equal to pivot
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        # Move `end` backward if the current element is greater than pivot
        while elements[end] > pivot:
            end -= 1

        # Swap elements if `start` is still less than `end`
        if start < end:
            swap(start, end, elements)

    # Swap the pivot element with the element at `end` to place it correctly
    swap(pivot_index, end, elements)
    return end  # Return the pivot's final position


def quick_sort(elements, start, end):
    """
    Recursively applies quicksort on subarrays divided by the pivot.
    """
    if start < end:
        pi = partition(elements, start, end)  # Partition the array
        quick_sort(elements, start, pi - 1)  # Recursively sort left partition
        quick_sort(elements, pi + 1, end)  # Recursively sort right partition


if __name__ == "__main__":
    elements = [11, 9, 8, 29, 7, 2, 33, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array:", elements)
