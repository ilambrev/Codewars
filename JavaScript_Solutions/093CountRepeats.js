function countRepeats(str) {
    let result = 0;

    for (let i = 1; i < str.length; i++) {
        if (str.charAt(i) === str.charAt(i - 1)) {
            result++;
        }
    }

    return result;
}

// console.log(countRepeats('abbbbc'));
// console.log(countRepeats('abbcca'));
// console.log(countRepeats('ab cca'));