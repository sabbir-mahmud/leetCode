def two_pointer(nums, target):
    """
    Brute-force approach using nested loops.
    Finds two numbers in nums that sum up to the target.

    Time Complexity: O(n^2) - Due to the nested loops iterating over all pairs.
    Space Complexity: O(1) - No extra space used apart from input storage.

    :param nums: List[int] - Input list of numbers.
    :param target: int - Target sum.
    :return: List[int] - Indices of two numbers that sum up to the target.
    """
    for i in range(len(nums)):  # O(n)
        for j in range(
            i + 1, len(nums)
        ):  # O(n) - Avoid checking same element and duplicate pairs
            if nums[i] + nums[j] == target:
                return [i, j]
    return -1  # Return -1 if no pair found


def using_hash_table(nums, target):
    """
    Optimized approach using a hash table (dictionary).
    Finds two numbers in nums that sum up to the target in linear time.

    Time Complexity: O(n) - We traverse the list once.
    Space Complexity: O(n) - We store elements in a dictionary.

    :param nums: List[int] - Input list of numbers.
    :param target: int - Target sum.
    :return: List[int] - Indices of two numbers that sum up to the target.
    """
    indexes = {}  # Dictionary to store numbers and their indices
    for index, num in enumerate(nums):  # O(n)
        complement = target - num  # Find the number needed to reach the target
        if complement in indexes:
            return [
                indexes[complement],
                index,
            ]  # Return the indices of the matching pair
        indexes[num] = index  # Store current number's index in dictionary
    return -1  # Return -1 if no pair found


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force:", two_pointer(nums, target))
    print("Optimized Hash Table:", using_hash_table(nums, target))
