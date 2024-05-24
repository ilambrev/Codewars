function squareSum(numbers) {
    return numbers.reduce((acc, curr) => {
        acc += curr * curr;

        return acc;
    }, 0);
}

// console.log(squareSum([1, 2, 2]));