function cleanString(s) {
    let result = '';

    for (let i = 0; i < s.length; i++) {
        const currentChar = s.charAt(i);
        if (currentChar == '#' && result.length > 0) {
            result = result.slice(0, result.length - 1);
        } else if (currentChar != '#') {
            result += currentChar;
        }
    }

    return result;
}

// console.log(cleanString('abc#d##c'));
// console.log(cleanString('abc##d######'));
// console.log(cleanString('#######'));
// console.log(cleanString(''));