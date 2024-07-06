function beggars(values, n) {
    if (n == 0) {
        return [];
    }

    const result = Array(n).fill(0);
    let counter = 0;

    for (let i = 0; i < values.length; i++) {
        if (counter > n - 1) {
            counter = 0;
        }
        result[counter] += values[i];
        counter++;
    }

    return result;
}

// console.log(beggars([1, 2, 3, 4, 5], 0));
// console.log(beggars([1, 2, 3, 4, 5], 1));
// console.log(beggars([1, 2, 3, 4, 5], 2));
// console.log(beggars([1, 2, 3, 4, 5], 3));
// console.log(beggars([1, 2, 3, 4, 5], 4));
// console.log(beggars([1, 2, 3, 4, 5], 5));
// console.log(beggars([1, 2, 3, 4, 5], 6));