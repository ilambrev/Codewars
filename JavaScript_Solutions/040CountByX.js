function countBy(x, n) {
    return Array.from({ length: n }, (_, n) => (n + 1) * x);
}

// console.log(countBy(1, 10));
// console.log(countBy(2, 5));