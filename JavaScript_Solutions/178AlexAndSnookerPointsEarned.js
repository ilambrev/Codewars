function frame(balls) {
    const blz = {
        'R': 1,
        'Y': 2,
        'G': 3,
        'Bn': 4,
        'Be': 5,
        'P': 6,
        'Bk': 7,
        'W': 0,
    }

    if (balls.includes('W')) {
        return 'Foul';
    }

    const regexp = /[B,G,P,R,Y]{1}[e,k,n]{0,1}[0-9]*/g;
    let score = 0;

    const records = [...balls.matchAll(regexp)];

    for (let i = 0; i < records.length; i++) {
        let currentRecord = records[i][0];
        let ball = '';
        let numberOfBalls = 1;

        if (currentRecord.charAt(0) == 'B') {
            ball = currentRecord.substring(0, 2);
            if (currentRecord.length > 2) {
                numberOfBalls = Number(currentRecord.substring(2));
            }
        } else {
            ball = currentRecord.substring(0, 1);
            if (currentRecord.length > 1) {
                numberOfBalls = Number(currentRecord.substring(1));
            }
        }

        score += blz[ball] * numberOfBalls;
    }

    if (score > 147) {
        return 'invalid data';
    } else {
        return score;
    }
}

// console.log(frame('R15P3G1Bk4Y1Bn1Be3'));
// console.log(frame('R13Bk14YRGBnBkRBePBk1'));
// console.log(frame('G9G11P9Bn2Bn1Be10G7WBn10G3'));
// console.log(frame('Bn14Bn14Bn8P9'));
// console.log(frame('R15Bk15YGBnBePBk'));
// console.log(frame('Bk16YGBnBeP'));
// console.log(frame('R9RGBn4BkRBeP'));
// console.log(frame('R15Bk16GYGBnBWeP'));
// console.log(frame('R8Bk17YGBnBk5BePBk1'));