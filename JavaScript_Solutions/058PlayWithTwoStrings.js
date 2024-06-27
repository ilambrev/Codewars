function workOnStrings(a, b) {
    const stringASymbolsCount = countSymbols(a);
    const stringBSymbolsCount = countSymbols(b);
    const regex = /[a-z]/;

    function countSymbols(str) {
        return str.split('').reduce((acc, curr) => {
            curr = curr.toLowerCase();

            if (!acc.hasOwnProperty(curr)) {
                acc[curr] = 0;
            }

            acc[curr] += 1;

            return acc;
        }, {});
    }

    function changeCase(str, symbolsCount) {
        return str.split('').reduce((acc, curr) => {
            if (symbolsCount.hasOwnProperty(curr.toLowerCase()) && symbolsCount[curr.toLowerCase()] % 2 != 0) {
                curr = regex.test(curr) ? curr.toUpperCase() : curr.toLowerCase();
            }

            acc += curr;

            return acc;
        }, '');
    }

    return changeCase(a, stringBSymbolsCount) + changeCase(b, stringASymbolsCount);
}

// console.log(workOnStrings('abc', 'cde'));
// console.log(workOnStrings('ab', 'aba'));
// console.log(workOnStrings('abab', 'bababa'));