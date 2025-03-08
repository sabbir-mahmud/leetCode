/**
 * Brute-force approach: Rotate the array one step at a time.
 * Time Complexity: O(k * n) - Inefficient for large arrays.
 * Space Complexity: O(1) - Modifies the array in place.
 */
const rotateArrayBruteForce = (nums, k) => {
    k = k % nums.length; // Handle cases where k > nums.length
    for (let i = 0; i < k; i++) {
        let lastEl = nums.pop(); // Remove last element
        nums.unshift(lastEl); // Insert at the beginning (O(n) operation)
    }
};

/**
 * Optimized approach: Rotate the array using slicing and `splice()`.
 * Time Complexity: O(n) - Only two slicing operations.
 * Space Complexity: O(n) - `splice()` creates a new array internally.
 */
const rotateArray = (nums, k) => {
    k = k % nums.length; // Handle cases where k > nums.length
    nums.splice(0, 0, ...nums.splice(-k)); // Move last k elements to the front
};

// Example usage
let nums1 = [1, 2, 3, 4, 5, 6, 7];
let k1 = 3;
rotateArrayBruteForce(nums1, k1);
console.log("Array after brute-force rotation -->", nums1);

let nums2 = [1, 2, 3, 4, 5, 6, 7];
let k2 = 3;
rotateArray(nums2, k2);
console.log("Array after optimized slicing -->", nums2);
