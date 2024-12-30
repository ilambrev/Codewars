function powerSumDigTerm(n) {
    const nums = [];

    for (let i = 2; i <= 100; i++) {
        let result = i;
        for (let j = 2; j <= 10; j++) {
            result = result * i;
            let digitsSum = result.toString()
            .split('')
            .reduce((acc, curr) => acc + Number(curr), 0);

            if (digitsSum == i) {
                nums.push(result);
            }
        }
    }

    nums.sort((n1, n2) => n1 - n2);

    return nums[n - 1];
}

// console.log(powerSumDigTerm(1));
// console.log(powerSumDigTerm(2));
// console.log(powerSumDigTerm(3));
// console.log(powerSumDigTerm(4));