const cardFaces = {
    'A': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
}

const cardSuits = {
    'c': 0,
    'd': 1,
    'h': 2,
    's': 3,
}


function encode(input) {
    const cardValue = (face, suit) => cardFaces[face] + 13 * cardSuits[suit];

    return input.map(card => cardValue(...card.split(''))).sort((v1, v2) => v1 - v2);
}

function decode(input) {
    const findCardByValue = (value) => {
        const suit = Math.floor(value / 13);
        const face = value % 13;
        return Object.keys(cardFaces).find(f => cardFaces[f] == face) + Object.keys(cardSuits).find(s => cardSuits[s] == suit);
    };

    return input.sort((v1, v2) => v1 - v2).map(findCardByValue);
}

// console.log(encode(['Ac', 'Ks', '5h', 'Td', '3c']));
// console.log(encode(['5h', '7c', 'Qh', 'Qs', 'Ad']));
// console.log(encode(['Td', '8c', 'Ks']));
// console.log(encode(['Qh', '5h', 'Ad']));
// console.log(encode(['8c', 'Ks', 'Td']));
// console.log(encode(['Qh', 'Ad', '5h']));

// console.log(decode([0, 51, 30, 22, 2]));
// console.log(decode([7, 22, 51]));
// console.log(decode([13, 30, 37]));
// console.log(decode([7, 51, 22]));
// console.log(decode([13, 37, 30]));
// console.log(decode([50, 6, 13, 30, 37]));