function moveZeros(arr) {
    const resultArr = [];
    const zeros = [];

    arr.forEach(e => e === 0 ? zeros.push(e) : resultArr.push(e));

    return resultArr.concat(zeros);
}

// console.log(moveZeros([false, 1, 0, 1, 2, 0, 1, 3, "a"]));