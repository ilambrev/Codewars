function computeRanks(number, games) {
    const positions = Array(number).fill(1);
    const teamsScores = Array.from({ length: number }, () => ({
        teamNum: 0,
        points: 0,
        for: 0,
        against: 0,

        gd() {
            return this.for - this.against;
        }
    }));

    teamsScores.forEach((t, i) => t.teamNum = i);

    for (const game of games) {
        const [teamA, teamB, goalA, goalB] = [...game];

        teamsScores[teamA].for += goalA;
        teamsScores[teamA].against += goalB;
        teamsScores[teamA].points += goalA > goalB ? 2 : goalA == goalB ? 1 : 0;

        teamsScores[teamB].for += goalB;
        teamsScores[teamB].against += goalA;
        teamsScores[teamB].points += goalA < goalB ? 2 : goalA == goalB ? 1 : 0;
    }

    teamsScores.sort((t1, t2) => {
        if (t2.points > t1.points) {
            return 1;
        } else if (t2.points < t1.points) {
            return -1;
        } else if (t2.gd() > t1.gd()) {
            return 1;
        } else if (t2.gd() < t1.gd()) {
            return -1;
        } else if (t2.for > t1.for) {
            return 1;
        } else if (t2.for < t1.for) {
            return -1;
        } else {
            return 0;
        }
    });

    let place = 1;

    for (let i = 0; i < teamsScores.length; i++) {
        if (i > 0 && (
            teamsScores[i - 1].points > teamsScores[i].points ||
            teamsScores[i - 1].gd() > teamsScores[i].gd() ||
            teamsScores[i - 1].for > teamsScores[i].for
        )) {

            place = i + 1;
        }

        positions[teamsScores[i].teamNum] = place;
    }

    return positions;
}

// console.log(computeRanks(6,
//     [[0, 5, 2, 2],
//     [1, 4, 0, 2],
//     [2, 3, 1, 2],
//     [1, 5, 2, 2],
//     [2, 0, 1, 1],
//     [3, 4, 1, 1],
//     [2, 5, 0, 2],
//     [3, 1, 1, 1],
//     [4, 0, 2, 0]]
// ));
// console.log(computeRanks(6,
//     [[0, 5, 2, 0],
//     [1, 4, 2, 2],
//     [2, 3, 1, 3],
//     [1, 5, 0, 0],
//     [2, 0, 2, 1],
//     [3, 4, 3, 1]]
// ));
// console.log(computeRanks(4,
//     [[0, 3, 1, 1],
//     [1, 2, 2, 2],
//     [1, 3, 2, 0],
//     [2, 0, 2, 0]]
// ));
// console.log(computeRanks(10, []));
// console.log(computeRanks(8, [[0, 7, 2, 0]]));