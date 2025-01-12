function distribute(gifts, socks) {
    const sortedGifts = gifts.sort((g1, g2) => g2 - g1);
    const sortedSocks = socks
        .reduce((acc, curr, i) => {
            acc.push([i, curr]);
            return acc;
        }, [])
        .sort((s1, s2) => s1[1] - s2[1]);
    const maxlength = Math.max(sortedGifts.length, sortedSocks.length);
    const minLength = Math.min(sortedGifts.length, sortedSocks.length);
    const result = [];

    for (let i = 0; i < maxlength; i++) {
        if (i < minLength) {
            if (i % 2 == 0) {
                result.push([sortedSocks[i / 2][0], sortedGifts[i / 2]]);
            } else {
                result.push([sortedSocks[sortedSocks.length - 1 - ((i - 1) / 2)][0], sortedGifts[sortedGifts.length - 1 - ((i - 1) / 2)]]);
            }
        } else if (sortedSocks.length > i) {
            if (i % 2 == 0) {
                result.push([sortedSocks[i / 2][0], 0]);
            } else {
                result.push([sortedSocks[sortedSocks.length - 1 - ((i - 1) / 2)][0], 0]);
            }
        } else {
            break;
        }
    }

    return result.sort((g1, g2) => g1[0] - g2[0]).map(g => g[1]);
}

// console.log(distribute([1, 2, 3], [1, 2, 3])); // [3, 2, 1]
// console.log(distribute([1, 2], [1, 2, 3])); // [2, 0, 1]
// console.log(distribute([1, 2, 3, 4], [1, 2, 3])); // [4, 3, 1]
// console.log(distribute([4, 5, 2, 3, 1], [5, 6, 4, 3, 1, 2])); // [2, 1, 0, 3, 5, 4]