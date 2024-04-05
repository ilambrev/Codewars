function highAndLow(numbers) {
    const sortedNums = numbers.split(/\s+/).map(n => Number(n)).sort((n1, n2) => n2 - n1);

    return `${sortedNums[0]} ${sortedNums[sortedNums.length - 1]}`;
}

// console.log(highAndLow('1 2 3 4 5'));
// console.log(highAndLow('1 2 -3 4 5'));
// console.log(highAndLow('1 9 3 4 -5'));