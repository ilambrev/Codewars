function arrayPlusArray(arr1, arr2) {
    return arr1.reduce((acc, curr) => acc + curr, 0) +
        arr2.reduce((acc, curr) => acc + curr, 0);
}

// console.log(arrayPlusArray([1, 2, 3], [4, 5, 6]));
// console.log(arrayPlusArray([-1, -2, -3], [-4, -5, -6]));
// console.log(arrayPlusArray([0, 0, 0], [4, 5, 6]));
// console.log(arrayPlusArray([100, 200, 300], [400, 500, 600]));