function duplicateCount(text) {

    const symbols = text
        .toLowerCase()
        .split('')
        .reduce((acc, curr) => {
            if (!acc.hasOwnProperty(curr)) {
                acc[curr] = 0;
            }

            acc[curr] += 1;

            return acc;
        }, {})

    return Object.values(symbols).filter(v => v > 1).length;
}

// console.log(duplicateCount('abcde'));
// console.log(duplicateCount('aabbcde'));
// console.log(duplicateCount('aabBcde'));
// console.log(duplicateCount('indivisibility'));
// console.log(duplicateCount('Indivisibilities'));
// console.log(duplicateCount('aA11'));
// console.log(duplicateCount('ABBA'));