function decode(r) {
    const numAsString = r.split('')
        .filter(symbol => symbol.charCodeAt(0) >= 48 && symbol.charCodeAt(0) <= 57)
        .join('');
    const num = Number(numAsString);
    const encodedText = r.slice(numAsString.length);

    let decodedText = '';

    function calculateDecoddedLetterValue(letterValue, num) {
        const remainder = num % 26;
        let decodedLetterValue;
        let counter = 0;

        for (let i = 0; i <= 25; i++) {
            let result = remainder * i % 26;
            if (result == letterValue) {
                counter++;
                decodedLetterValue = i;
            }
        }

        return counter == 1 ? decodedLetterValue : -1;
    }

    for (let i = numAsString.length; i < r.length; i++) {
        const decodedLetterValue = calculateDecoddedLetterValue(r.charCodeAt(i) - 97, num);

        if (decodedLetterValue == -1) {
            return 'Impossible to decode';
        } else {
            decodedText += String.fromCharCode(decodedLetterValue + 97);
        }
    }

    return decodedText;
}

// console.log(decode('1273409kuqhkoynvvknsdwljantzkpnmfgf'));
// console.log(decode('1544749cdcizljymhdmvvypyjamowl'));
// console.log(decode('105860ymmgegeeiwaigsqkcaeguicc'));
// console.log(decode('1122305vvkhrrcsyfkvejxjfvafzwpsdqgp'));
// console.log(decode('5057aan'));