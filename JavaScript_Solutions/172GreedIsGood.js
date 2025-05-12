function score(dice) {
    const matches = {};
    for (let i = 0; i < dice.length; i++) {
        if (!matches.hasOwnProperty(dice[i])) {
            matches[dice[i]] = 0;
        }
        matches[dice[i]] += 1;
    }

    let result = 0;

    for (const [key, value] of Object.entries(matches)) {
        const threeOfType = Math.floor(value / 3);
        switch (key) {
            case '1':
                result += threeOfType * 1000 + (value - threeOfType * 3) * 100;
                break;
            case '2':
                result += threeOfType * 200;
                break;
            case '3':
                result += threeOfType * 300;
                break;
            case '4':
                result += threeOfType * 400;
                break;
            case '5':
                result += threeOfType * 500 + (value - threeOfType * 3) * 50;
                break;
            case '6':
                result += threeOfType * 600;
                break;
        }
    }

    return result;
}

// console.log(score([5, 1, 3, 4, 1]));
// console.log(score([1, 1, 1, 3, 1]));
// console.log(score([2, 4, 4, 5, 4]));
// console.log(score([2, 3, 4, 6, 2]));
// console.log(score([4, 4, 4, 3, 3]));