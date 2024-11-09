// # Input: x = 121
// # Output: true
// # Explanation: 121 reads as 121 from left to right and from right to left.
// # Example 2:

// # Input: x = -121
// # Output: false
// # Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// # Example 3:

// # Input: x = 10
// # Output: false
// # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

// with str functions
// const is_palindrome = (number) => {
//     let string_number = number.toString();
//     return string_number === string_number.split("").reverse().join("");
// };

// without str
const is_palindrome = (number) => {
    original_number = number;
    compare_number = 0;

    while (number > 0) {
        compare_number = compare_number * 10 + (number % 10);
        number = Math.floor(number / 10);
    }

    return original_number == compare_number;
};

const result = is_palindrome(121);
console.log(result);
