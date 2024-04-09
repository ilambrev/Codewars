function descendingOrder(n) {
    return Number(n.toString().split('').map(Number).sort((d1, d2) => d2 - d1).join(''));
}

// console.log(descendingOrder(42145));
// console.log(descendingOrder(145263));
// console.log(descendingOrder(123456789));