function digitize(n) {
    return n.toString().split('').map(Number).reverse();
}

// console.log(digitize(35231));
// console.log(digitize(0));