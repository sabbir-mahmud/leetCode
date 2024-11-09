// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// const longest_prefix = (strs) => {
//     strs.sort();
//     let prefix = "";

//     for (let i = 0; i < strs[0].length; i++) {
//         let char = strs[0][i];

//         for (let j = 0; j < strs.length; j++) {
//             if (strs[j][i] != char) {
//                 return prefix;
//             }
//         }
//         prefix += char;
//     }
//     return prefix;
// };

const longest_prefix = (strs) => {
    strs.sort();
    let prefix = "";

    for (let i = 0; i < strs[0].length; i++) {
        if (strs[0][i] != strs[strs.length - 1][i]) {
            return prefix;
        }
        prefix += strs[0][i];
    }
    return prefix;
};

const result = longest_prefix(["flower", "flow", "flight"]);
console.log("result --> ", result);
