def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Uses the sliding window technique with a set to efficiently track characters.

    Time Complexity: O(n) - Each character is processed at most twice (once added and once removed).
    Space Complexity: O(min(n, 26)) - Stores unique characters, at most 26 if only lowercase English letters are used.

    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    char_set = set()  # Set to store unique characters in the current window
    left = 0  # Left pointer of the sliding window
    max_length = 0  # Stores the maximum length found

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If character at right pointer is in the set, shrink window from the left
        if s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set
        char_set.add(s[right])

        # Update max_length with the current window size
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    test_string = "abcdefabcbb"
    print(
        "Longest Substring Without Repeating Characters -->",
        length_of_longest_substring(test_string),
    )
