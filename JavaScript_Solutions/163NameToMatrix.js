const matrixfy = str => {
    if (str.length == 0) {
        return 'name must be at least one letter';
    }

    let matrixDimension = Math.ceil(Math.sqrt(str.length));

    if (str.length < matrixDimension * matrixDimension) {
        str = str + '.'.repeat((matrixDimension * matrixDimension) - str.length);
    }

    let result = [];

    for (let i = 0; i < str.length; i += matrixDimension) {
        let row = [];
        for (let j = i; j < i + matrixDimension; j++) {
            row.push(str.charAt(j));
        }
        result.push(row);
    }

    return result;
};

// console.log(matrixfy(''));
// console.log(matrixfy('Bill'));
// console.log(matrixfy('Frank'));
// console.log(matrixfy('A'));
// console.log(matrixfy('Franklin'));