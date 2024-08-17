function onlyDuplicates(str) {
    const letterMap = str.split('').reduce((acc, curr) => {
        if (!acc.hasOwnProperty(curr)) {
            acc[curr] = 0;
        }

        acc[curr] += 1;

        return acc;
    }, {});

    const removeLetter = (letter) => str = str.replace(letter, '');

    Object.entries(letterMap).filter(([k, v]) => v == 1).forEach(([k, v]) => removeLetter(k));

    return str;
}

// console.log(onlyDuplicates('abccdefee'));