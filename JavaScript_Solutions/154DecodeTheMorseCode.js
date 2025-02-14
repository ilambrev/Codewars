// let MORSE_CODE = {
//     '....': 'H',
//     '.': 'E',
//     '-.--': 'Y',
//     '.---': 'J',
//     '..-': 'U',
//     '-..': 'D',
// };

decodeMorse = function (morseCode) {
    morseCode = morseCode.trim();
    const result = morseCode.split('   ').reduce((acc, curr) => {
        const word = curr.split(' ').map(letterCode => MORSE_CODE[letterCode]).join('');
        acc.push(word);

        return acc;
    }, []).join(' ');

    return result;
}

// console.log(decodeMorse('.... . -.--   .--- ..- -.. .'));
// console.log(decodeMorse('   .... . -.--   '));