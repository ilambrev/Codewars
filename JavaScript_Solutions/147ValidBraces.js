function validBraces(braces) {
    const bracesSymbols = {
        '(': ')',
        '[': ']',
        '{': '}',
    };

    if (braces.length % 2 !== 0) {
        return false;
    }

    const bracesArr = braces.split('');

    while (bracesArr.length > 0) {
        if (!bracesSymbols.hasOwnProperty(bracesArr[0])) {
            return false;
        }
        let indexOfOpenBrace = 0;
        while (indexOfOpenBrace < bracesArr.length) {
            if (bracesSymbols.hasOwnProperty(bracesArr[indexOfOpenBrace + 1])) {
                indexOfOpenBrace++;
            } else {
                break;
            }
        }
        if (indexOfOpenBrace == bracesArr.length - 1) {
            return false;
        }
        const indexOfCloseBrace = bracesArr.indexOf(bracesSymbols[bracesArr[indexOfOpenBrace]], indexOfOpenBrace + 1);
        if (indexOfCloseBrace == -1 || (indexOfCloseBrace - indexOfOpenBrace) % 2 == 0) {
            return false;
        }
        bracesArr.splice(indexOfCloseBrace, 1);
        bracesArr.splice(indexOfOpenBrace, 1);
    }

    return true;
}

// console.log(validBraces('()))'));
// console.log(validBraces('()'));
// console.log(validBraces('[]'));
// console.log(validBraces('{}'));
// console.log(validBraces('(){}[]'));
// console.log(validBraces('([{}])'));
// console.log(validBraces('(}'));
// console.log(validBraces('[(])'));
// console.log(validBraces('({})[({})]'));
// console.log(validBraces('(})'));
// console.log(validBraces('(({{[[]]}}))'));
// console.log(validBraces('{}({})[]'));
// console.log(validBraces(')(}{]['));
// console.log(validBraces('())({}}{()][]['));
// console.log(validBraces('(((({{'));
// console.log(validBraces('}}]]))}])'));