function lettersToNumbers(s) {
    const score = s.split('').reduce((acc, curr) => {
        let code = curr.charCodeAt(0);

        if (code >= 48 && code <= 57) {
            code -= 48;
        } else if (code >= 65 && code <= 90) {
            code = (code - 64) * 2;
        } else if (code >= 97 && code <= 122) {
            code -= 96;
        } else {
            code = 0;
        }

        acc += code;

        return acc;
    }, 0);

    return score;
}

// console.log(lettersToNumbers('I Love You'));
// console.log(lettersToNumbers('ILoveYou'));
// console.log(lettersToNumbers('ARE YOU HUNGRY?'));
// console.log(lettersToNumbers('oops, i did it again!'));
// console.log(lettersToNumbers('Give me 5!'));
// console.log(lettersToNumbers('Give me five!'));