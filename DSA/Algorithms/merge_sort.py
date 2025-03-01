def merge_two_sorted_lists(a, b, arr):
    """
    Merges two sorted lists 'a' and 'b' into 'arr' in sorted order.

    Parameters:
    a (list): First sorted sublist.
    b (list): Second sorted sublist.
    arr (list): The main list where the merged elements will be stored.
    """
    len_a, len_b = len(a), len(b)
    i = j = k = 0  # Pointers for 'a', 'b', and 'arr'

    # Merge elements from both lists into 'arr' in sorted order
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # Copy any remaining elements from 'a'
    arr[k:] = a[i:]

    # Copy any remaining elements from 'b'
    arr[k + len(a[i:]) :] = b[j:]


def merge_sort(arr):
    """
    Sorts the given list 'arr' using the merge sort algorithm.

    Parameters:
    arr (list): The list to be sorted.
    """
    if len(arr) <= 1:
        return  # Base case: A list of 0 or 1 elements is already sorted

    mid = len(arr) // 2  # Find the middle index
    left = arr[:mid]  # Left half
    right = arr[mid:]  # Right half

    merge_sort(left)  # Recursively sort the left half
    merge_sort(right)  # Recursively sort the right half
    merge_two_sorted_lists(left, right, arr)  # Merge the sorted halves


# Merge Sort for Dictionaries (Sorting by a Specific Key)
def merge_two_sorted_lists_exercise(left, right, key="name", descending=False):
    """
    Merges two sorted lists of dictionaries based on a given key.

    Parameters:
    left (list): Left sorted list.
    right (list): Right sorted list.
    key (str): The dictionary key used for sorting.
    descending (bool): Sort order (True for descending, False for ascending).

    Returns:
    list: Merged sorted list.
    """
    merged = []
    i, j = 0, 0  # Pointers for left and right lists

    while i < len(left) and j < len(right):
        if (
            (left[i][key] >= right[j][key])
            if descending
            else (left[i][key] <= right[j][key])
        ):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from both lists
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort_exercise(elements, key="name", descending=False):
    """
    Sorts a list of dictionaries based on a given key using merge sort.

    Parameters:
    elements (list): List of dictionaries to be sorted.
    key (str): Dictionary key to sort by.
    descending (bool): Sort order (True for descending, False for ascending).

    Returns:
    list: Sorted list of dictionaries.
    """
    if len(elements) <= 1:
        return elements

    mid = len(elements) // 2
    left = merge_sort_exercise(elements[:mid], key, descending)
    right = merge_sort_exercise(elements[mid:], key, descending)
    return merge_two_sorted_lists_exercise(left, right, key, descending)


if __name__ == "__main__":
    # Test merge_sort with a numeric list
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    merge_sort(arr)
    print("Sorted List:", arr)

    # Test merge_sort_exercise with a list of dictionaries
    elements = [
        {"name": "vedanth", "age": 17, "time_hours": 1},
        {"name": "rajab", "age": 12, "time_hours": 3},
        {"name": "vignesh", "age": 21, "time_hours": 2.5},
        {"name": "chinmay", "age": 24, "time_hours": 1.5},
    ]
    sorted_elements = merge_sort_exercise(elements, key="time_hours", descending=True)
    print("Sorted by time_hours (descending):", sorted_elements)
