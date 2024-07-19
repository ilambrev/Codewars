function rank(st, we, n) {
    if (st == '') {
        return 'No participants';
    }

    const participants = st.split(',');

    if (n > participants.length) {
        return 'Not enough participants';
    }

    const participantsWithWinningNums = participants.reduce((acc, curr, i) => {
        const name = curr.toUpperCase();
        const letterWeightsSum = name.split('')
            .map(l => 1 + l.charCodeAt(0) - 'A'.charCodeAt(0))
            .reduce((acc, curr) => acc += curr, 0);
        const som = curr.length + letterWeightsSum;
        const winningNumber = som * we[i];
        acc[curr] = winningNumber;
        return acc;
    }, {});

    function compareNames(name1, name2) {
        if (participantsWithWinningNums[name1] < participantsWithWinningNums[name2]) {
            return 1;
        } else if (participantsWithWinningNums[name1] > participantsWithWinningNums[name2]) {
            return -1;
        } else {
            return name1.localeCompare(name2);
        }
    }

    return participants.sort((name1, name2) => compareNames(name1, name2))[n - 1];
}

// console.log(rank('COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH', [1, 4, 4, 5, 2, 1], 4));
// console.log(rank('Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin', [4, 2, 1, 4, 3, 1, 2], 4));
// console.log(rank('Lagon,Lily', [1, 5], 2));
// console.log(rank('Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin', [4, 2, 1, 4, 3, 1, 2], 8));
// console.log(rank('', [4, 2, 1, 4, 3, 1, 2], 6));