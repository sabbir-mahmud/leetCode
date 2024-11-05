# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# using O(n2)
# def run(nums, target):
#     for index, value in enumerate(nums):
#         for i in range(index + 1, len(nums)):
#             if value + nums[i] == target:
#                 return [index, i]
#     return None


# using O(n)
def run(nums, target):
    nums_index = {}
    for index, i in enumerate(nums):
        complement = target - i
        if complement in nums_index:
            return [nums_index[complement], index]
        nums_index[i] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    indexes = run(nums, target)
    print(indexes)
