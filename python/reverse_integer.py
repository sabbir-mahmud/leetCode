"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


def reverse_integer(x: int):
    """
    Time Complexity:
    - O(log(x)), where `x` is the absolute value of the input integer.
    - Each iteration processes one digit, and the number of digits in `x` is logarithmic in base 10, so the time complexity is proportional to the number of digits.

    Space Complexity:
    - O(1) (constant space).
    - We only use a few variables (`reversed_x`, `sign`, `m`) to store intermediate values, which does not depend on the size of the input number.
    """
    # Constants for the minimum and maximum 32-bit integer values
    MIN_INT, MAX_INT = (2**31, 2**31 - 1)  # -2147483648 and 2147483647

    # Initialize the reversed number and the sign of the input number
    reversed_x = 0
    sign = -1 if x < 0 else 1  # Store the sign to handle negative numbers
    x = abs(x)  # Work with the absolute value of x for simplicity

    # Process each digit until x becomes 0
    while x != 0:
        m = x % 10  # Get the last digit of x
        x //= 10  # Remove the last digit from x

        # Check for overflow before updating the reversed number
        if reversed_x > (MAX_INT - m) // 10:
            return 0  # Return 0 if reversing would cause overflow

        # Build the reversed number by shifting the digits and adding the new digit
        reversed_x = (reversed_x * 10) + m

    # Return the reversed number, adjusting for the original sign
    return sign * reversed_x


if __name__ == "__main__":
    x = 123456274375754
    print(reverse_integer(x))  # Example usage

    # Example Runs:
    # 123 -> 321
    # -123 -> -321
    # 120 -> 21
