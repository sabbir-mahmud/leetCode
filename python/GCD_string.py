"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

"""


# Define a function that finds the greatest common divisor (GCD) string of str1 and str2.
# The GCD string is the longest string that can be repeated to form both str1 and str2.
def gcdOfStrings(str1: str, str2: str):
    # Get the lengths of str1 and str2 and store them in l1 and l2 for later use.
    # Example: str1 = "ABCABC" -> l1 = 6, str2 = "ABC" -> l2 = 3
    l1, l2 = len(str1), len(str2)

    # Loop over possible lengths (i) from the smaller string's length down to 1.
    # We start with the max possible length to find the *greatest* common divisor first.
    # min(l1, l2) ensures we don’t exceed the shorter string’s length.
    for i in range(min(l1, l2), 0, -1):
        # Check if i divides both l1 and l2 evenly (no remainder).
        # This is like finding a common factor in numbers; the substring length must work for both.
        # Example: l1 = 6, l2 = 3, i = 3 -> 6 % 3 = 0 and 3 % 3 = 0 (true)
        if l1 % i == 0 and l2 % i == 0:
            # Calculate how many times a substring of length i repeats in str1 (t1) and str2 (t2).
            # Use integer division (//) to get the exact number of repetitions.
            # Example: l1 = 6, i = 3 -> t1 = 6 // 3 = 2; l2 = 3, i = 3 -> t2 = 3 // 3 = 1
            t1, t2 = l1 // i, l2 // i
            # Test if the substring str1[:i] (first i characters of str1) can form both strings:
            # - str1[:i] * t1 must equal str1 (reconstructs str1).
            # - str1[:i] * t2 must equal str2 (reconstructs str2).
            # Example: str1 = "ABCABC", str2 = "ABC", i = 3 -> "ABC" * 2 = "ABCABC", "ABC" * 1 = "ABC"
            if str1[:i] * t1 == str1 and str1[:i] * t2 == str2:
                # If the condition passes, str1[:i] is the GCD string. Return it.
                # Since we start with the largest i, this is the longest valid divisor.
                # Example: Returns "ABC" for str1 = "ABCABC", str2 = "ABC"
                return str1[:i]

    # If no common divisor is found after checking all possible lengths, return an empty string.
    # Example: str1 = "ABC", str2 = "DEF" -> no common substring -> return ""
    return ""


if __name__ == "__main__":
    print(gcdOfStrings("ABABAB", "ABAB"))
