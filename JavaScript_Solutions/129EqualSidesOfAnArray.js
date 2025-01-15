function findEvenIndex(arr) {
    let index = -1;

    for (let i = 0; i < arr.length; i++) {
        const leftSum = calculateLeftSum(arr, i);
        const rightSum = calculateRightSum(arr, i);

        if (leftSum == rightSum) {
            index = i;
            break;
        }
    }

    function calculateLeftSum(arr, currentIndex) {
        return arr.reduce((acc, curr, i) => {
            if (i < currentIndex) {
                acc += curr;
            }
            return acc;
        }, 0);
    }

    function calculateRightSum(arr, currentIndex) {
        return arr.reduce((acc, curr, i) => {
            if (i > currentIndex) {
                acc += curr;
            }
            return acc;
        }, 0);
    }

    return index;
}

// console.log(findEvenIndex([1, 2, 3, 4, 3, 2, 1]));
// console.log(findEvenIndex([1, 100, 50, -51, 1, 1]));
// console.log(findEvenIndex([1, 2, 3, 4, 5, 6]));
// console.log(findEvenIndex([20, 10, 30, 10, 10, 15, 35]));