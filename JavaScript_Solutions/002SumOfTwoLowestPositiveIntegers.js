function sumTwoSmallestNumbers(numbers) {
    return numbers.sort((n1, n2) => n1 - n2).slice(0,2).reduce((n1, n2) => n1 + n2);
}

// console.log(sumTwoSmallestNumbers([19, 5, 42, 2, 77]));
// console.log(sumTwoSmallestNumbers([10, 343445353, 3453445, 3453545353453]));
// console.log(sumTwoSmallestNumbers([5, 8, 12, 19, 22]));
// console.log(sumTwoSmallestNumbers([15, 28, 4, 2, 43]));
// console.log(sumTwoSmallestNumbers([3, 87, 45, 12, 7]));
// console.log(sumTwoSmallestNumbers([23, 71, 33, 82, 1]));
// console.log(sumTwoSmallestNumbers([52, 76, 14, 12, 4]));