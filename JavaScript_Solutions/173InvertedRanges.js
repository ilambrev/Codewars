function invertedRanges(ranges) {
    const rowBetweenBounds = Array(101).fill(0);
    if (ranges.lenght == 0) {
        return [[0, 100]];
    }

    const result = [];

    for (let i = 0; i < ranges.length; i++) {
        for (let j = ranges[i][0]; j <= ranges[i][1]; j++) {
            rowBetweenBounds[j] = 1;
        }
    }

    for (let i = 0; i < rowBetweenBounds.length; i++) {
        const invertedRange = [];
        if (rowBetweenBounds[i] == 0) {
            invertedRange.push(rowBetweenBounds[i]);
            for (let j = i + 1; j < rowBetweenBounds.length; j++) {
                if (rowBetweenBounds[j] == 1) {
                    result.push([i, j - 1]);
                    i = j;
                    break;
                }

                if (j == rowBetweenBounds.length - 1 && rowBetweenBounds[j] == 0) {
                    result.push([i, j]);
                    i = j;
                    break;
                }
            }
        }
    }

    return result;
}

// console.log(invertedRanges([[0, 100]]));
// console.log(invertedRanges([[0, 50], [51, 100]]));
// console.log(invertedRanges([]));
// console.log(invertedRanges([[0, 25], [51, 75]]));
// console.log(invertedRanges([[25, 50]]));