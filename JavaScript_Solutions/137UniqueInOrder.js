const uniqueInOrder = function (iterable) {
    const result = [];
    if (iterable.length > 0) {
        result.push(iterable[0]);
        for (let i = 0; i < iterable.length - 1; i++) {
            if (iterable[i + 1] !== result[result.length - 1]) {
                result.push(iterable[i + 1]);
            }
        }
    }

    return result;
}

// console.log(uniqueInOrder('AAAABBBCCDAABBB'));
// console.log(uniqueInOrder('ABBCcAD'));
// console.log(uniqueInOrder([1, 2, 2, 3, 3]));