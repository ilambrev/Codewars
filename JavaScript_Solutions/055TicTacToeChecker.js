function isSolved(board) {
    const xWinPattern = '111';
    const oWinPattern = '222';
    const combinations = {
        1: board[0].join(''),
        2: board[1].join(''),
        3: board[2].join(''),
        4: '' + board[0][0] + board[1][0] + board[2][0],
        5: '' + board[0][1] + board[1][1] + board[2][1],
        6: '' + board[0][2] + board[1][2] + board[2][2],
        7: '' + board[0][0] + board[1][1] + board[2][2],
        8: '' + board[0][2] + board[1][1] + board[2][0],
    };

    if (checkForWinner(xWinPattern)) {
        return 1;
    } else if (checkForWinner(oWinPattern)) {
        return 2;
    }

    for (let i = 0; i < board.length; i++) {
        const emptyFields = board[i].filter(f => f === 0).length;

        if (emptyFields > 0) {
            return -1;
        }
    }

    function checkForWinner(pattern) {
        return Object.values(combinations).filter(v => v === pattern).length > 0 ? true : false;
    }

    return 0;
}

// console.log(isSolved([
//     [0, 0, 1],
//     [0, 1, 2],
//     [2, 1, 0]
// ]));