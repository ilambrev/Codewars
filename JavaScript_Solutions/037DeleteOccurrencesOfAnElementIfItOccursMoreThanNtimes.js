function deleteNth(arr, n) {
    const motifs = {};

    return arr.reduce((acc, curr) => {
        if (motifs.hasOwnProperty(curr)) {
            motifs[curr] += 1;
        } else {
            motifs[curr] = 1;
        }

        if (motifs[curr] <= n) {
            acc.push(curr);
        }

        return acc;
    }, [])
}

// console.log(deleteNth([1, 2, 3, 1, 2, 1, 2, 3], 2));
// console.log(deleteNth([20, 37, 20, 21], 1));