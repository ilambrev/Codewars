function toCamelCase(str) {
    const words = str.split(/[-_]/).map((word, i) => {
        if (i > 0) {
            word = word.charAt(0).toUpperCase() + word.slice(1, word.length);
        }

        return word;
    });

    return words.join('');
}

// console.log(toCamelCase('the-stealth-warrior'));
// console.log(toCamelCase('The_Stealth_Warrior'));
// console.log(toCamelCase('The_Stealth-Warrior'));