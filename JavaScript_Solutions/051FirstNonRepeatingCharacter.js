function firstNonRepeatingLetter(s) {
    let result = '';

    const symbols = {};

    const lowerCaseSymbols = s.toLowerCase().split('');

    lowerCaseSymbols.forEach(symbol => {
        if (!symbols.hasOwnProperty(symbol)) {
            symbols[symbol] = 0;
        }

        symbols[symbol] += 1;
    });

    for (let i = 0; i < lowerCaseSymbols.length; i++) {
        if (symbols[lowerCaseSymbols[i]] == 1) {
            result = s.charAt(i);
            break
        }
    }

    return result;
}

// console.log(firstNonRepeatingLetter('stress'));
// console.log(firstNonRepeatingLetter('sTreSS'));