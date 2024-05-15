function order(words) {
    if (words === '') {
        return '';
    } else {
        const wordsArr = words.split(' ');

        return wordsArr.sort((w1, w2) => {
            const firstDigit = Number(w1.split('').sort()[0]);
            const secondDigit = Number(w2.split('').sort()[0]);

            if (firstDigit < secondDigit) {
                return -1;
            } else if (firstDigit > secondDigit) {
                return 1;
            } else {
                return 0;
            }
        }).join(' ');
    }
}

// console.log(order('is2 Thi1s T4est 3a'));
// console.log(order('4of Fo1r pe6ople g3ood th5e the2'));
// console.log(order(''));