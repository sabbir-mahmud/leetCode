const reverseInteger = (x) => {
    // Constants for the minimum and maximum 32-bit integer values
    const MIN_INT = -(2 ** 31); // -2147483648
    const MAX_INT = 2 ** 31 - 1; // 2147483647

    // Determine the sign of the number and work with its absolute value
    const sign = x < 0 ? -1 : 1; // Store the sign for later multiplication
    let rev = 0; // Initialize the reversed number to 0
    x = Math.abs(x); // Work with the absolute value to simplify the reversal logic

    // Process each digit of the number until x becomes 0
    while (x !== 0) {
        let m = x % 10; // Get the last digit
        x = Math.floor(x / 10); // Remove the last digit from the number

        // Check for overflow by verifying if the new rev would be out of range
        if (rev > Math.floor((MAX_INT - m) / 10)) {
            return 0; // Return 0 in case of overflow
        }
        rev = rev * 10 + m; // Build the reversed number
    }

    // Return the reversed number multiplied by the sign to restore the original sign
    return sign * rev;
};

// Example Runs:
console.log(reverseInteger(123)); // 321
console.log(reverseInteger(-123)); // -321
console.log(reverseInteger(120)); // 21 (leading zeroes are removed)
console.log(reverseInteger(12344566778900)); // 0 (overflow)

/*
Time Complexity:
- O(log(x)), where `x` is the absolute value of the input integer.
- Each iteration processes one digit, and the number of digits in `x` is logarithmic in base 10, so the time complexity is proportional to the number of digits.

Space Complexity:
- O(1) (constant space).
- We only use a few variables (`rev`, `sign`, `m`) to store intermediate values, which does not depend on the size of the input number.
*/
