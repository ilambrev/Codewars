function incrementString(string) {
    let digits = string.split('').reverse().join('').match(/[0-9]+/gm);
    let result = '';

    if (digits != null) {
        digits = digits[0].split('').reverse().join('');
        result = string.substring(0, string.length - digits.length);

        const initilaNumberOfDigits = digits.length;
        let number = Number(digits) + 1;
        const currentNumberOfDigits = number.toString().length;

        if (currentNumberOfDigits < initilaNumberOfDigits) {
            result += '0'.repeat(initilaNumberOfDigits - currentNumberOfDigits);
        }

        result += number;
    } else {
        result += string + 1;
    }

    return result;
}

// console.log(incrementString('foo'));
// console.log(incrementString('foobar23'));
// console.log(incrementString('foo0042'));
// console.log(incrementString('foo9'));
// console.log(incrementString('foo099'));