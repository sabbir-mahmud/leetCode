# Initial array to be sorted
arr = [34, 55, 623, 344, 124, 1324, 533, 6565, 122, 345, 665, 12]


# Function to implement Bubble Sort using nested loops
def bubble_sort_using_loop(arr: list):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm.

    Parameters:
        arr (list): The list of integers to sort.

    Steps:
    1. Compare adjacent elements in the array.
    2. Swap them if the left element is greater than the right element.
    3. Continue this process for all elements in decreasing order of pass length.
    4. Break early if no swaps are made during a pass (array is already sorted).
    """
    size = len(arr) - 1  # Determine the number of passes required
    for i in range(size):  # Outer loop for the number of passes
        swapped = False  # Flag to check if any swaps were made in this pass

        for j in range(size - i):  # Inner loop to compare adjacent elements
            # Compare and swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                # Perform the swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred

        # If no swaps were made in this pass, the array is already sorted
        if not swapped:
            break


# Call the bubble sort function
bubble_sort_using_loop(arr)

# Print the sorted array
print("Bubble sort using loops --> ", arr)
