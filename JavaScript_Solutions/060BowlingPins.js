function bowlingPins(arr) {
    const pins = [
        ['I', ' ', 'I', ' ', 'I', ' ', 'I'],
        [' ', 'I', ' ', 'I', ' ', 'I', ' '],
        [' ', ' ', 'I', ' ', 'I', ' ', ' '],
        [' ', ' ', ' ', 'I', ' ', ' ', ' ']
    ];

    const positions = {
        1: [3, 3],
        2: [2, 2],
        3: [2, 4],
        4: [1, 1],
        5: [1, 3],
        6: [1, 5],
        7: [0, 0],
        8: [0, 2],
        9: [0, 4],
        10: [0, 6],
    }

    arr.forEach(pin => pins[positions[pin][0]][positions[pin][1]] = ' ');

    return pins.map(r => r.join('')).join('\n');
}

// console.log(bowlingPins([3, 5, 9]));