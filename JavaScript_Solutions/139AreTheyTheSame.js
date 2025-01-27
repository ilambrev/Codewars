function comp(array1, array2) {
    if (!array1 || !array2 || array1.length != array2.length) {
        return false;
    }

    array1.sort((n1, n2) => n1 - n2);
    array2.sort((n1, n2) => n1 - n2);

    for (let i = 0; i < array1.length; i++) {
        if (array2[i] != array1[i] * array1[i]) {
            return false;
        }
    }

    return true;
}

// console.log(comp(
//     [121, 144, 19, 161, 19, 144, 19, 11],
//     [121, 14641, 20736, 361, 25921, 361, 20736, 361]
// ));
// console.log(comp(
//     [121, 144, 19, 161, 19, 144, 19, 11],
//     [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
// ));
// console.log(comp(
//     [2, 2, 3],
//     [4, 9, 9]
// ));