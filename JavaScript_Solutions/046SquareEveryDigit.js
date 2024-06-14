function squareDigits(num) {
    return Number(num
        .toString()
        .split('')
        .map(d => Math.pow(Number(d), 2))
        .join(''));
}

// console.log(squareDigits(9119));
// console.log(squareDigits(765));