function findOdd(A) {
    const result = A.reduce((acc, curr) => {
        if (!acc.hasOwnProperty(curr)) {
            acc[curr] = 0;
        }
        acc[curr] += 1;

        return acc;
    }, {});

    return Number(Object.entries(result).filter(([_, value]) => value % 2 != 0)[0][0]);
}

// console.log(findOdd([7]));
// console.log(findOdd([0]));
// console.log(findOdd([1, 1, 2]));
// console.log(findOdd([0, 1, 0, 1, 0]));
// console.log(findOdd([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]));