function interleave(...args) {
    const maxLength = Math.max(...args.map(a => a.length));
    const result = [];

    for (let i = 0; i < maxLength; i++) {
        for (let j = 0; j < args.length; j++) {
            if (args[j].length < i + 1) {
                result.push(null);
            } else {
                result.push(args[j][i]);
            }
        }
    }

    return result;
}

// console.log(interleave([1, 2, 3], ['c', 'd', 'e']));
// console.log(interleave([1, 2, 3], [4, 5]));
// console.log(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9]));
// console.log(interleave([]));