function averageString(str) {
    const namesToDigits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    const numNames = str.split(' ');
    let sum = 0;

    if (!str) {
        return 'n/a';
    }

    for (let i = 0; i < numNames.length; i++) {
        if (!namesToDigits.hasOwnProperty(numNames[i])) {
            return 'n/a';
        }

        sum += namesToDigits[numNames[i]];
    }

    const average = Math.floor(sum / numNames.length);

    return Object.entries(namesToDigits).find(([k, v]) => v == average)[0];
}

// console.log(averageString('zero nine five two'));
// console.log(averageString('four six two three'));
// console.log(averageString('four six two three'));
// console.log(averageString('five four'));
// console.log(averageString('zero zero zero zero zero'));
// console.log(averageString('one one eight one'));
// console.log(averageString(''));