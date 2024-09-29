function separateLiquids(glass) {
    const densities = {
        H: 1.36,
        W: 1.00,
        A: 0.87,
        O: 0.80,
    }

    if (glass.length > 0) {
        const rowLength = glass[0].length;
        const tempArr = glass.reduce((acc, curr) => {
            acc.push(...curr);
            return acc;
        }, []).sort((l1, l2) => densities[l1] - densities[l2]);

        glass.length = 0;

        for (let i = 0; i < tempArr.length / rowLength; i++) {
            const row = [];
            for (let j = 0; j < rowLength; j++) {
                row.push(tempArr[rowLength * i + j]);
            }
            glass.push(row);
        }
    }

    return glass;
}

// console.log(separateLiquids([['H', 'H', 'W', 'O'], ['W', 'W', 'O', 'W'], ['H', 'H', 'O', 'O']]));
// console.log(separateLiquids([['A', 'A', 'O', 'H'], ['A', 'H', 'W', 'O'], ['W', 'W', 'A', 'W'], ['H', 'H', 'O', 'O']]));
// console.log(separateLiquids([['A', 'H', 'W', 'O']]));
// console.log(separateLiquids([['A'], ['H'], ['W'], ['O']]));
// console.log(separateLiquids([]));