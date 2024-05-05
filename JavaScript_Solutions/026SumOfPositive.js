function positiveSum(arr) {

    return arr.reduce((acc, curr) => curr > 0 ? acc + curr : acc, 0);
}

// console.log(positiveSum([1, -4, 7, 12]));