function solution(number) {
    const romeSymbols = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    };

    let result = '';

    function mapToRomeNumeral(multiplayer, n) {
        let romeRepresentation = '';
        if (multiplayer == 1000) {
            romeRepresentation += romeSymbols[1000].repeat(n);
        } else {
            romeRepresentation += n == 9 ? romeSymbols[multiplayer] + romeSymbols[multiplayer * 10] :
                n < 9 && n >= 5 ? romeSymbols[multiplayer * 5] + romeSymbols[multiplayer].repeat(n - 5) :
                    n == 4 ? romeSymbols[multiplayer] + romeSymbols[multiplayer * 5] : romeSymbols[multiplayer].repeat(n);
        }
        number -= n * multiplayer;

        return romeRepresentation;
    }

    while (number > 0) {
        if (number >= 1000) {
            result += mapToRomeNumeral(1000, Math.floor(number / 1000));
        } else if (number < 1000 && number > 99) {
            result += mapToRomeNumeral(100, Math.floor(number / 100));
        } else if (number < 100 && number > 9) {
            result += mapToRomeNumeral(10, Math.floor(number / 10));
        } else if (number < 10 && number > 0) {
            result += mapToRomeNumeral(1, number);
        }
    }

    return result;
}

// console.log(solution(1));
// console.log(solution(2));
// console.log(solution(3));
// console.log(solution(4));
// console.log(solution(5));
// console.log(solution(9));
// console.log(solution(10));
// console.log(solution(11));
// console.log(solution(19));
// console.log(solution(22));
// console.log(solution(15));
// console.log(solution(1000));
// console.log(solution(1001));
// console.log(solution(1990));
// console.log(solution(2007));
// console.log(solution(2008));