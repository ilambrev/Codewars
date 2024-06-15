function persistence(num) {
    let multiplicationsNum = 0;

    while (num > 9) {
        multiplicationsNum++;
        num = num
            .toString()
            .split('')
            .map(Number)
            .reduce((acc, curr) => acc *= curr, 1);
    }

    return multiplicationsNum;
}

// console.log(persistence(39));
// console.log(persistence(999));
// console.log(persistence(4));