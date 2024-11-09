# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# def longest_prefix(strs: list[str]):
#     strs.sort()
#     prefix = ""

#     for i in range(len(strs[0])):
#         char = strs[0][i]

#         for string in strs:
#             if i >= len(string) or string[i] != char:
#                 return prefix

#         prefix += char
#     return prefix


def longest_prefix(strs: list[str]):
    strs.sort()
    prefix = ""

    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            return prefix
        prefix += strs[0][i]
    return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    result = longest_prefix(strs)
    print("result --> ", result)
