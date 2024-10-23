// function randInt(min, max) {
//     return Math.floor((max - min + 1) * Math.random());
// }

// function toShuffled(array) {
//     const shuffled = array.slice();
//     for (let i = 0; i < array.length; i++) {
//         const j = randInt(0, array.length - 1);
//         [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
//     }
//     return shuffled;
// }

// class MasterMind {
//     static #MAX_ATTEMPTS = 60;
//     static COLOURS = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"];
//     #solution;
//     #attempts = 0;
//     status = {
//         isOver: false, won: false, message:
//             'the game is still ongoing, check() was not called with the solution'
//     };

//     constructor(solution) {
//         this.#solution = solution.slice();
//     }

//     check(attempt) {
//         if (this.status.isOver)
//             throw new Error('this game is over, calling check() has no effect');

//         // input validation
//         if (!Array.isArray(attempt) || attempt.length != 4 ||
//             ![...attempt].every(color => MasterMind.COLOURS.includes(color))
//         ) {
//             this.status = {
//                 isOver: true, won: false, message:
//                     'expected an array of 4 valid colours, but got: '
//                     + JSON.stringify(attempt)
//             };
//             throw new RangeError(this.status.message);
//         }

//         // attempts count
//         this.#attempts += 1;
//         if (this.#attempts > MasterMind.#MAX_ATTEMPTS) {
//             this.status = {
//                 isOver: true, won: false, message: 'too many attempts !'
//             };
//             throw new Error(this.status.message);
//         }

//         // calculate hints
//         const countsRef = {}, countsUser = {};
//         const hints = [];
//         for (let i = 0; i < this.#solution.length; i++) {
//             const exp = this.#solution[i], act = attempt[i];
//             if (act === exp) {
//                 hints.push('Black');
//             } else {
//                 countsRef[exp] = (countsRef[exp] ?? 0) + 1;
//                 countsUser[act] = (countsUser[act] ?? 0) + 1;
//             }
//         }
//         for (const color in countsRef)
//             for (let i = 0; i < Math.min(countsRef[color], countsUser[color] ?? 0); i++)
//                 hints.push('White');

//         // win check
//         if (hints.length === 4 && hints.every(hint => hint === 'Black')) {
//             this.status = { isOver: true, won: true, message: 'the player wins' };
//             return 'WON!';
//         }

//         // normal return
//         return toShuffled(hints);
//     }
// };

// My solution
function mastermind(game) {
    const colors = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"];

    const matchedColors = [];
    const unmatchedColors = [];
    const matchedColorsCounter = () => matchedColors.reduce((acc, curr) => acc += curr[1], 0);
    const colorsPositions = {};
    let answer = '';

    for (let color of colors) {
        const testArray = new Array(4).fill(color);
        answer = game.check(testArray);

        if (answer == 'WON!') {
            for (let i = 0; i < 4; i++) {
                colorsPositions[i] = testArray[i];
            }
            break;
        }

        if (answer.length > 0) {
            matchedColors.push([color, answer.length]);
        } else {
            unmatchedColors.push(color);
        }

        if (matchedColorsCounter == 4) {
            break;
        }
    }

    while (Object.keys(colorsPositions).length < 4) {
        const unmatchedColor = unmatchedColors[0];

        for (let [color] of matchedColors) {
            for (let i = 0; i < 4; i++) {
                const testArray = new Array(4).fill(unmatchedColor);
                testArray[i] = color;
                answer = game.check(testArray);

                if (answer[0] == 'Black' && !colorsPositions.hasOwnProperty(i)) {
                    colorsPositions[i] = color;
                    break;
                }

            }
        }
    }

    if (answer != 'WON!') {
        console.log(game.check(Object.entries(colorsPositions)
            .sort(([k1, v1], [k2, v2]) => k1 - k2)
            .map(([k, v]) => v)));
    } else {
        console.log(answer);
    }
}

// function doTest(solution) {
//     const game = new MasterMind(solution);

//     mastermind(game);
// }

// doTest(['Red', 'Red', 'Yellow', 'Blue']);
// doTest(['Red', 'Red', 'Red', 'Red']);