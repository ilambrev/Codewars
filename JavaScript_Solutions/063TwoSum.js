function twoSum(numbers, target) {
    result = [];

    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if (numbers[i] + numbers[j] == target) {
                result.push(i, j);
                return result;
            }
        }
    }
    return result;
}

// console.log(twoSum([1, 2, 3], 4));
// console.log(twoSum([3, 2, 4], 6));