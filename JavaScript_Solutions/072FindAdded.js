function findAdded(st1, st2) {
    function countNums(str) {
        return str.split('').map(Number).reduce((acc, curr) => {
            if (!acc.hasOwnProperty(curr)) {
                acc[curr] = 0;
            }
            acc[curr] += 1;
            return acc;
        }, {});
    }

    const st1Nums = countNums(st1);
    const st2Nums = countNums(st2);

    const result = [];

    Object.entries(st2Nums).forEach(([k, v]) => {
        let missingNums = 0;
        if (!st1Nums.hasOwnProperty(k)) {
            missingNums = v;
        } else {
            missingNums = v - st1Nums[k];
        }

        if (missingNums > 0) {
            result.push(...Array(missingNums).fill(k));
        }

    });

    return result.sort().join('');
}

// console.log(findAdded('4455446', '447555446666'));
// console.log(findAdded('44554466', '447554466'));
// console.log(findAdded('9876521', '9876543211'));
// console.log(findAdded('678', '876'));
// console.log(findAdded('678', '6'));