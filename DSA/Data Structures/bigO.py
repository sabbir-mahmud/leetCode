"""
Big O Notation Summary

This file contains key notes and examples about Big O notation for analyzing algorithm complexity.

Summary:
- Big O notation is used to describe the performance or complexity of an algorithm.
- It measures the worst-case scenario in terms of time and space as the input size grows.

Examples of Complexity:
- O(1): Constant time, irrespective of input size.
- O(log n): Logarithmic time, often seen in divide-and-conquer algorithms like binary search.
- O(n): Linear time, proportional to the input size.
- O(n log n): Linearithmic time, common in efficient sorting algorithms like mergesort.
- O(n^2): Quadratic time, typical in algorithms with nested loops.
- O(2^n): Exponential time, found in recursive solutions like the Fibonacci sequence.
- O(n!): Factorial time, seen in permutations or combinations.

This file demonstrates these complexities with code examples and discusses the performance of various data structures.

Each example includes steps on how to calculate the complexity:
- Count the number of operations relative to input size.
- Identify loops, recursion, and any dominant term in compound expressions.
- Consider both time and space aspects for a comprehensive understanding.
"""

# Big O Notation Examples and Notes


def constant_time_example(arr):
    """
    O(1) - Constant Time
    Accessing an element in an array by index.

    How to calculate:
    - Only one operation is performed irrespective of input size.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return arr[0]  # Always takes the same amount of time


def logarithmic_time_example(arr, target):
    """
    O(log n) - Logarithmic Time
    Binary search implementation.

    How to calculate:
    - The array is repeatedly divided into halves until the target is found or the array is empty.
    - Logarithmic operations occur due to halving (base 2 logarithm).

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_time_example(arr):
    """
    O(n) - Linear Time
    Iterating through an array.

    How to calculate:
    - A single loop iterates through all elements once.
    - The number of iterations is proportional to the size of the input (n).

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for element in arr:
        print(element)


def linearithmic_time_example(arr):
    """
    O(n log n) - Linearithmic Time
    Using Python's built-in sorted function (Timsort).

    How to calculate:
    - Sorting involves multiple passes through the input (n) combined with merging (log n).

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    return sorted(arr)


def quadratic_time_example(arr):
    """
    O(n^2) - Quadratic Time
    Nested loops iterating over the same input.

    How to calculate:
    - Outer loop runs n times.
    - Inner loop runs n times for each iteration of the outer loop.
    - Total operations: n * n = n^2.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


def exponential_time_example(n):
    """
    O(2^n) - Exponential Time
    Fibonacci sequence using recursion.

    How to calculate:
    - Each function call generates two more calls, doubling the work at each level.
    - Total operations grow as powers of 2.

    Time Complexity: O(2^n)
    Space Complexity: O(n) (due to recursion stack)
    """
    if n <= 1:
        return n
    return exponential_time_example(n - 1) + exponential_time_example(n - 2)


def factorial_time_example(arr):
    """
    O(n!) - Factorial Time
    Generating all permutations of an array.

    How to calculate:
    - For n elements, there are n! permutations.
    - Recursive backtracking or library functions iterate through all possible arrangements.

    Time Complexity: O(n!)
    Space Complexity: O(n!) (to store permutations)
    """
    from itertools import permutations

    return list(permutations(arr))


# Big O Data Structures Performance Table
DATA_STRUCTURES_PERFORMANCE = {
    "Array": {"Access": "O(1)", "Search": "O(n)", "Insert/Delete": "O(n)"},
    "Linked List": {"Access": "O(n)", "Search": "O(n)", "Insert/Delete": "O(1)"},
    "Hash Table": {"Access": "O(1)", "Search": "O(1)", "Insert/Delete": "O(1)"},
    "Binary Search Tree": {
        "Access": "O(log n)",
        "Search": "O(log n)",
        "Insert/Delete": "O(log n)",
    },
    "Heap": {"Access": "O(1)", "Search": "O(n)", "Insert/Delete": "O(log n)"},
}

if __name__ == "__main__":
    # Example usage of the functions

    # O(1) example
    print("Constant Time Example:", constant_time_example([10, 20, 30]))

    # O(log n) example
    print("Logarithmic Time Example:", logarithmic_time_example([1, 2, 3, 4, 5], 4))

    # O(n) example
    print("Linear Time Example:")
    linear_time_example([1, 2, 3, 4, 5])

    # O(n log n) example
    print("Linearithmic Time Example:", linearithmic_time_example([5, 3, 1, 4, 2]))

    # O(n^2) example
    print("Quadratic Time Example:")
    quadratic_time_example([1, 2, 3])

    # O(2^n) example
    print("Exponential Time Example:", exponential_time_example(5))

    # O(n!) example
    print("Factorial Time Example:", factorial_time_example([1, 2, 3]))

    # Display Big O Data Structures Performance Table
    print("\nBig O Data Structures Performance Table:")
    for structure, operations in DATA_STRUCTURES_PERFORMANCE.items():
        print(f"{structure}: {operations}")
