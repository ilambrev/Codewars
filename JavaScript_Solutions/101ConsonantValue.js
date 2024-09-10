function solve(s) {
    const offset = 96;
    const consonants = new Set(['a', 'e', 'i', 'o', 'u']);
    let highestValue = 0;
    let currentValue = 0;

    for (let i = 0; i < s.length; i++) {
        if (!consonants.has(s.charAt(i))) {
            currentValue += s.charCodeAt(i) - offset;
            if (i == s.length - 1 && currentValue > highestValue) {
                highestValue = currentValue;
            }
        } else {
            if (currentValue > highestValue) {
                highestValue = currentValue;
            }
            currentValue = 0;
        }
    }

    return highestValue;
};

// console.log(solve('zodiacs'));
// console.log(solve('strength'));
// console.log(solve('az'));