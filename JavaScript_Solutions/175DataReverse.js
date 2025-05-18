function dataReverse(data) {
    let result = [];
    for (let i = data.length - 1; i >= 0; i -= 8) {
        const octet = data.slice(i - 7, i + 1);
        result = result.concat(octet);
    }

    return result;
}

// console.log(dataReverse([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]));
// console.log(dataReverse([0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]));