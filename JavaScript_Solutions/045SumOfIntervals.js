function sumIntervals(intervals) {
    const sortedIntervals = intervals.sort((i1, i2) => {
        if (i1[0] < i2[0]) return -1;
        if (i1[0] > i2[0]) return 1;

        if (i1[1] < i2[1]) return -1;
        if (i1[1] > i2[1]) return 1;

        return 0;
    });

    let result = 0;
    let begin = 0;
    let end = 0;

    if (sortedIntervals.length > 0) {
        begin = sortedIntervals[0][0];
        end = sortedIntervals[0][1];
    }

    for (let i = 0; i < sortedIntervals.length; i++) {
        const currentInterval = sortedIntervals[i];
        if (currentInterval[0] <= end && currentInterval[1] > end) {
            end = currentInterval[1];
        } else if (currentInterval[1] > end) {
            result += end - begin;
            begin = currentInterval[0];
            end = currentInterval[1];
        }

        if (i == sortedIntervals.length - 1) {
            result += end - begin;
        }
    }

    return result;
}

/*
console.log(sumIntervals(
    [
        [1, 5],
    ]
));
console.log(sumIntervals(
    [
        [1, 4],
        [7, 10],
        [3, 5]
    ]
));
console.log(sumIntervals(
    [
        [1, 2],
        [6, 10],
        [11, 15]
    ]
));
console.log(sumIntervals(
    [
        [1, 4],
        [7, 10],
        [3, 5]
    ]
));
console.log(sumIntervals(
    [
        [1, 5],
        [10, 20],
        [1, 6],
        [16, 19],
        [5, 11]
    ]
));
console.log(sumIntervals(
    [
        [0, 20],
        [-100000000, 10],
        [30, 40]
    ]
));
*/