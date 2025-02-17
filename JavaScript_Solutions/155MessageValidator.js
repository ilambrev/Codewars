function isAValidMessage(message) {
    if (message.length == 0) {
        return true;
    }

    let testedText = '';

    let regexp = /((?<digits>[0-9]+)(?<letters>[A-Za-z]+))/g;
    let matches = message.matchAll(regexp);

    for (let match of matches) {
        let { digits, letters } = match.groups;
        if (Number(digits) != letters.length) {
            return false;
        }
        testedText += digits + letters;
    }

    return message == testedText;
}

// console.log(isAValidMessage('3hey5hello2hi'));
// console.log(isAValidMessage('4code13hellocodewars'));
// console.log(isAValidMessage('3hey5hello2hi5'));
// console.log(isAValidMessage('code4hello5'));
// console.log(isAValidMessage('1a2bb3ccc4dddd5eeeee'));
// console.log(isAValidMessage(''));