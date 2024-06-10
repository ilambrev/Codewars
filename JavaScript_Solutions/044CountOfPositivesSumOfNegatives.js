function countPositivesSumNegatives(input) {

    if (input == null || input.length == 0) {
        return [];
    }

    let countOfPositiveNums = 0;
    let sumOfNegativeNums = 0;

    input.forEach(n => {
        if (n > 0) {
            countOfPositiveNums++;
        }

        if (n < 0) {
            sumOfNegativeNums += n;
        }
    });

    return [countOfPositiveNums, sumOfNegativeNums];
}

// console.log(countPositivesSumNegatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]));