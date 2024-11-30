const solution = function (firstArray, secondArray) {
    let arrLength = firstArray.length;
    let sum = 0;

    for (let i = 0; i < arrLength; i++) {
        const difference = Math.max(firstArray[i], secondArray[i]) - Math.min(firstArray[i], secondArray[i]);
        const squareValue = Math.pow(difference, 2);
        sum += squareValue;
    }

    return sum / arrLength;
}

// console.log(solution([1, 2, 3], [4, 5, 6]));
// console.log(solution([10, 20, 10, 2], [10, 25, 5, -2]));
// console.log(solution([0, -1], [-1, 0]));