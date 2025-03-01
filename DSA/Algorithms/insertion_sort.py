def insertion_sort(elements):
    """
    Sorts a list using the insertion sort algorithm.

    Time Complexity:
    - Best case (already sorted): O(n)
    - Worst/Average case: O(n^2)

    Space Complexity: O(1) (in-place sorting)
    """
    for i in range(1, len(elements)):
        anchor = elements[i]  # Element to be placed at the correct position
        j = i - 1

        # Shift elements to the right to create space for anchor
        while j >= 0 and elements[j] > anchor:
            elements[j + 1] = elements[j]
            j -= 1

        # Insert anchor at the correct position
        elements[j + 1] = anchor


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(elements)
    print("Sorted list:", elements)
