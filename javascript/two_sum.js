//   Input: nums = [2,7,11,15], target = 9
//  Output: [0,1]
//  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// using O(n2)
// const run = (nums = [], target) => {
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] + nums[j] === target) {
//                 return [i, j];
//             }
//         }
//     }
// };

// using O(n)
const run = (nums = [], target) => {
    let num_index = {};
    for (let i = 0; i < nums.length; i++) {
        complement = target - nums[i];
        if (complement in num_index) {
            return [num_index[complement], i];
        }
        num_index[nums[i]] = i;
    }
};

const result = run([11, 15, 2, 7], 9);
console.log(result);
