function createTwoSetsOfEqualSum(n) {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        sum += i;
    }

    if (sum % 2 != 0) {
        return [];
    }

    let halfSum = sum / 2;

    const set1 = [];
    const set2 = [];

    for (let i = n; i >= 1; i--) {
        if (halfSum - i >= 0) {
            set2.push(i);
            halfSum -= i;
        } else {
            set1.push(i);
        }
    }

    return [set1.reverse(), set2.reverse()];
}

// console.log(createTwoSetsOfEqualSum(8));
// console.log(createTwoSetsOfEqualSum(9));