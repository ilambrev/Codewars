const makeChange = (amount) => {
    const coins = [[50, 'H'], [25, 'Q'], [10, 'D'], [5, 'N'], [1, 'P']];
    const change = {};

    for (let coin of coins) {
        const numOfCoins = Math.floor(amount / coin[0]);
        if (numOfCoins > 0) {
            amount -= numOfCoins * coin[0];
            change[coin[1]] = numOfCoins;
        }
    }

    return change;
};

// console.log(makeChange(0));
// console.log(makeChange(1));
// console.log(makeChange(43));
// console.log(makeChange(91));