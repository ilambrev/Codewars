function digPow(n, p) {
    const digits = n.toString().split('').map(Number);

    let result = digits.reduce((acc, curr, i) => {
        acc += Math.pow(curr, p + i);
        return acc;
    }, 0);

    return result % n === 0 ? result / n : -1;;
}

// console.log(digPow(89, 1));
// console.log(digPow(92, 1));
// console.log(digPow(695, 2));
// console.log(digPow(46288, 3));