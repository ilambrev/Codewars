function high(x) {

    let words = x.split(' ');
    let maxValue = 0;
    let wordWithMaxValue = '';

    for (let word of words) {

        let value = [...word].map(c => c.charCodeAt(0) - 96).reduce((c1, c2) => c1 + c2);

        if (value > maxValue) {

            maxValue = value;
            wordWithMaxValue = word;

        }

    }

    return wordWithMaxValue;

}

// console.log(high('man i need a taxi up to ubud'));
// console.log(high('what time are we climbing up the volcano'));
// console.log(high('take me to semynak'));
// console.log(high('aa b'));
// console.log(high('b aa'));
// console.log(high('bb d'));
// console.log(high('d bb'));
// console.log(high('aaa b'));