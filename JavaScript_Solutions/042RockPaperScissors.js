const rps = (p1, p2) => {
    let result = '';

    if (p1 === p2) {
        result = 'Draw!';
    } else if (p1 === 'scissors' && p2 === 'paper' || p1 === 'rock' && p2 === 'scissors' || p1 === 'paper' && p2 === 'rock') {
        result = 'Player 1 won!';
    } else {
        result = 'Player 2 won!';
    }

    return result;
};

// console.log(rps('scissors', 'paper'));
// console.log(rps('scissors', 'rock'));
// console.log(rps('paper', 'paper'));