"""

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000


Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

"""


def find_max_average(nums, k):
    # Step 1: Calculate the sum of the first window of size k
    window_sum = sum(nums[:k])  # Initial window: nums[0] to nums[k-1]
    max_sum = window_sum  # Store the maximum sum found so far

    # Step 2: Slide the window through the array from index k to the end
    for i in range(k, len(nums)):
        # Remove the element that is going out of the window (nums[i - k])
        # Add the new element that is coming into the window (nums[i])
        window_sum += nums[i] - nums[i - k]

        # Update max_sum if the new window_sum is greater
        max_sum = max(max_sum, window_sum)

    # Step 3: Return the maximum average by dividing max sum by k
    return max_sum / k
