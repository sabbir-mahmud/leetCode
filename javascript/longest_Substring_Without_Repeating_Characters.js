const lengthOfLongestSubstring = (s) => {
    /**
     * Finds the length of the longest substring without repeating characters.
     *
     * Uses the sliding window technique with a hash map to efficiently track characters.
     *
     * Time Complexity: O(n) - Each character is processed at most twice (once added, once removed).
     * Space Complexity: O(min(n, 26)) - At most 26 characters are stored if only lowercase English letters are used.
     *
     * @param {string} s - Input string
     * @return {number} - Length of the longest substring without repeating characters
     */
    const chars = {}; // Hash map to store the last seen index of each character
    let left = 0; // Left pointer of the sliding window
    let res = 0; // Stores the maximum length found

    // Iterate through the string with the right pointer
    for (let right = 0; right < s.length; right++) {
        // If character at right pointer is found in the map and within the window, move left pointer
        if (s[right] in chars && chars[s[right]] >= left) {
            left = chars[s[right]] + 1; // Move left pointer past the repeating character
        }

        // Store/update the last seen index of the current character
        chars[s[right]] = right;

        // Update max length with the current window size
        res = Math.max(res, right - left + 1);
    }

    return res;
};

const test_string = "abcabcbb";
console.log(
    "Longest Substring Without Repeating Characters -->",
    lengthOfLongestSubstring(test_string)
);
