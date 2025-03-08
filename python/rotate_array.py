"""
Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

"""


def rotate_array_brute_force(nums: list, k: int):
    """
    Brute-force approach: Rotate the array one step at a time.
    Time Complexity: O(k * n) - Very slow for large n and k.
    Space Complexity: O(1) - Modifies the array in place.
    """
    k = k % len(nums)  # Handle cases where k > len(nums)
    for _ in range(k):
        last_element = nums.pop()  # Remove last element
        nums.insert(0, last_element)  # Insert it at the beginning (O(n) operation)


def rotate_array(nums: list, k: int):
    """
    Optimized approach: Rotate the array using slicing.
    Time Complexity: O(n) - Only two slicing operations.
    Space Complexity: O(n) - Creates a new list before modifying nums.
    """
    k = k % len(nums)  # Handle cases where k > len(nums)
    nums[:] = nums[-k:] + nums[:-k]  # Move last k elements to the front


if __name__ == "__main__":
    # Brute-force method
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    rotate_array_brute_force(nums1, k1)
    print("Array after brute-force rotation -->", nums1)

    # Optimized slicing method
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    k2 = 3
    rotate_array(nums2, k2)
    print("Array after optimized slicing -->", nums2)
