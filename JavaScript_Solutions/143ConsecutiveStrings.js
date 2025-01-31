function longestConsec(strarr, k) {
    let longestString = "";

    if (k > 0 && strarr.length > 0 && k <= strarr.length) {
        for (let i = 0; i <= strarr.length - k; i++) {
            let currentString = strarr.slice(i, i + k).reduce((acc, curr) => acc + curr, "");
            if (currentString.length > longestString.length) {
                longestString = currentString;
            }
        }
    }

    return longestString;
}

// console.log(longestConsec(["zone", "abigail", "theta", "form", "libe", "zas"], 2));
// console.log(longestConsec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1));
// console.log(longestConsec([], 3));
// console.log(longestConsec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2));
// console.log(longestConsec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2));
// console.log(longestConsec(["zone", "abigail", "theta", "form", "libe", "zas"], -2));
// console.log(longestConsec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3));
// console.log(longestConsec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15));
// console.log(longestConsec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0));