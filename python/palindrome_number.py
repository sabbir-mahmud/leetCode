# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# with str
# def is_palindrome(number):
#     number = str(number)
#     return number == number[::-1]


# without str
def is_palindrome(number):
    original_number = number
    compare_number = 0
    while number > 0:
        end_number = number % 10
        compare_number = compare_number * 10 + end_number
        number //= 10

    return original_number == compare_number


if __name__ == "__main__":
    result = is_palindrome(121)
    print(result)
