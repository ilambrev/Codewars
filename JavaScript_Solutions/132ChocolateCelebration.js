function chocolateSplit(people, bars) {
    const barPieces = 16;

    if (typeof people != 'number' || typeof bars != 'number') {
        return 'Error. We need numbers.';
    }

    if (people <= 0) {
        return 'Nobody here. Skedaddle.';
    }

    let chocolatePieces = bars * barPieces;
    const groupA = Math.round(people * 0.2);
    const groupB = Math.round(people * 0.1);
    const groupC = Math.round(people * 0.05);
    const groupD = people - (groupA + groupB + groupC);
    const neededPiecesForPerson = 1;
    const result = [0, 0];

    const morePeacesNeeded = eatChocolate(groupD + groupC, neededPiecesForPerson);
    if (morePeacesNeeded > 0) {
        result.push('You should buy more chocolate next time');
        const neededBars = Math.round(morePeacesNeeded / barPieces) + 1 + bars;
        result.push(neededBars);
        return result;
    }

    eatChocolate(groupB, neededPiecesForPerson);

    for (let i = 1; i <= groupC; i++) {
        let isChocolateLeft = true;
        for (let j = 1; j <= 19; j++) {
            if (chocolatePieces - 1 >= 0) {
                chocolatePieces--;
            } else {
                isChocolateLeft = false;
                break;
            }
        }
        if (!isChocolateLeft) {
            break;
        }
    }

    result[1] = chocolatePieces;

    if (chocolatePieces > 16) {
        result.push('That was too much chocolate!');
        const neededBars = Math.round((groupB + groupC + groupD) / barPieces) + 1;
        result.push(neededBars);
    }

    function eatChocolate(groupOfPeople, neededPiecesForPerson) {
        while (groupOfPeople > 0 && chocolatePieces > 0) {
            if (chocolatePieces - neededPiecesForPerson >= 0) {
                result[0] += 1;
                groupOfPeople--;
                chocolatePieces -= neededPiecesForPerson;
            } else {
                return 0;
            }
        }
        return groupOfPeople;
    }

    return result;
}

// console.log(chocolateSplit(100, 10));
// console.log(chocolateSplit(1000, 10));
// console.log(chocolateSplit(8, 10));
// console.log(chocolateSplit(0, 10));
// console.log(chocolateSplit('blue', 10));
// console.log(chocolateSplit(8, [8, 7]));