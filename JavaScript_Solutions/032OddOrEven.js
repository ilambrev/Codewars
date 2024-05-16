function oddOrEven(array) {
    return array.reduce((acc, curr) => acc + curr, 0) % 2 === 0 ? 'even' : 'odd';
}

// console.log(oddOrEven([0]));
// console.log(oddOrEven([0, 1, 4]));
// console.log(oddOrEven([0, -1, -5]));