function isIntArray(arr) {
    if (Array.isArray(arr) && (arr.filter(e => !Number.isInteger(e)).length == 0 || arr.length == 0)) {
        return true;
    }

    return false;
}

// console.log(isIntArray([]));
// console.log(isIntArray([1, 2, 3, 4]));
// console.log(isIntArray([-11, -12, -13, -14]));
// console.log(isIntArray([1.0, 2.0, 3.0]));
// console.log(isIntArray([1, 2, NaN]));
// console.log(isIntArray(true));
// console.log(isIntArray(null));
// console.log(isIntArray(undefined));
// console.log(isIntArray(NaN));
// console.log(isIntArray(''));
// console.log(isIntArray([null]));
// console.log(isIntArray([undefined]));
// console.log(isIntArray([NaN]));
// console.log(isIntArray([1.0, 2.0, 3.0001]));
// console.log(isIntArray(['-1']));
// console.log(isIntArray([1.23e-7, 2]));
// console.log(isIntArray([1.2, 1.8, 3]));