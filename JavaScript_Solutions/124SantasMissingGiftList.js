// const GIFTS = {
//     1: 'Toy Soldier',
//     2: 'Wooden Train',
//     4: 'Hoop',
//     8: 'Chess Board',
//     16: 'Horse',
//     32: 'Teddy',
//     64: 'Lego',
//     128: 'Football',
//     256: 'Doll',
//     512: "Rubik's Cube"
// };

function gifts(number) {
    const sortedNums = Object.keys(GIFTS).sort((k1, k2) => k2 - k1);
    const toys = [];

    for (let i = 0; i < sortedNums.length; i++) {
        if (number >= sortedNums[i]) {
            number -= sortedNums[i];
            toys.push(GIFTS[sortedNums[i]]);
        }
        if (number == 0) {
            break;
        }
    }

    return toys.sort((t1, t2) => t1.localeCompare(t2));
}

// console.log(gifts(1));
// console.log(gifts(2));
// console.log(gifts(3));
// console.log(gifts(22));
// console.log(gifts(160));