function bingo(ticket, win) {
    let miniWins = 0

    for (let [string, num] of ticket) {
        for (let i = 0; i < string.length; i++) {
            if (string.charCodeAt(i) == Number(num)) {
                miniWins++;
                break;
            }
        }
    }

    return miniWins >= win ? 'Winner!' : 'Loser!';
}

// console.log(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2));
// console.log(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1));
// console.log(bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3));