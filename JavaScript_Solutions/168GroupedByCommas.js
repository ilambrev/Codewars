function groupByCommas(n) {
    const digits = n.toString().split('');
    const result = [];
    const digitsGroup = [];

    for (let i = digits.length - 1; i >= 0; i--) {
        if (digitsGroup.length == 3) {
            result.push(digitsGroup.reverse().join(''));
            digitsGroup.length = 0;
        }
        digitsGroup.push(digits[i]);
    }

    result.push(digitsGroup.reverse().join(''));

    return result.reverse().join(',');
}

// console.log(groupByCommas(1));
// console.log(groupByCommas(10));
// console.log(groupByCommas(100));
// console.log(groupByCommas(1000));
// console.log(groupByCommas(10000));
// console.log(groupByCommas(100000));
// console.log(groupByCommas(1000000));
// console.log(groupByCommas(35235235));