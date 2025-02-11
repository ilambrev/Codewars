function findOutlier(integers) {
    const numOfEvenNums = integers.slice(0, 3).filter(n => n % 2 == 0).length;
    if (numOfEvenNums > 1) {
        for (let num of integers) {
            if (num % 2 != 0) {
                return num;
            }
        }
    } else {
        for (let num of integers) {
            if (num % 2 == 0) {
                return num;
            }
        }
    }
}

// console.log(findOutlier([2, 4, 0, 100, 4, 11, 2602, 36]));
// console.log(findOutlier([160, 3, 1719, 19, 11, 13, -21]));
// console.log(findOutlier([0, 1, 2]));
// console.log(findOutlier([1, 2, 3]));
// console.log(findOutlier([2, 6, 8, 10, 3]));
// console.log(findOutlier([0, 0, 3, 0, 0]));
// console.log(findOutlier([1, 1, 0, 1, 1]));