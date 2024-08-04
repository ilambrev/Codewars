const runLengthEncoding = function (str) {
    const result = [];
    let currentSymbol = '';
    let counter = 0;

    for (let i = 0; i < str.length; i++) {
        if (str.charAt(i) == currentSymbol) {
            counter++;
        } else {
            if (currentSymbol) {
                result.push([counter, currentSymbol]);
            }

            currentSymbol = str.charAt(i);
            counter = 1;
        }

        if (i == str.length - 1) {
            result.push([counter, currentSymbol]);
        }
    }

    return result;
}

// console.log(runLengthEncoding('hello world!'));
// console.log(runLengthEncoding('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb'));