function sortArray(array) {
    const oddArr = array.filter(n => n % 2 !== 0).sort((n1, n2) => n1 - n2);
    const resultArr = [];

    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            resultArr.push(array[i]);
        } else {
            resultArr.push(oddArr.shift());
        }
    }

    return resultArr;
}

// console.log(sortArray([7, 1]));
// console.log(sortArray([5, 8, 6, 3, 4]));
// console.log(sortArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]));
// console.log(sortArray([1, 11, 2, 8, 3, 4, 5]));