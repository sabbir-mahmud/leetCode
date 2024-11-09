// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
// For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used

const roman_to_integer = (roman) => {
    const roman_numbers = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };
    let res = 0;
    for (let i = 0; i < roman.length; i++) {
        if (
            i + 1 < roman.length &&
            roman_numbers[roman[i]] < roman_numbers[roman[i + 1]]
        ) {
            res -= roman_numbers[roman[i]];
        } else {
            res += roman_numbers[roman[i]];
        }
    }
    return res;
};

const result = roman_to_integer("MCMXCIV");
console.log(result);
