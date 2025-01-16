function merryChristmas(s) {
    const pattern = 'MerryChristmas';
    let counter = 0;

    while (s.length > 0) {
        for (let i = 0; i < pattern.length; i++) {
            const index = s.indexOf(pattern.charAt(i));
            if (index > -1) {
                s = s.slice(0, index) + s.slice(index + 1);
            } else {
                return counter;
            }
        }
        counter++;
    }

    return counter;
}

// console.log(merryChristmas('MerryChristmas'));
// console.log(merryChristmas('ChristmasMerry'));
// console.log(merryChristmas('yrreMsamtsirhC'));
// console.log(merryChristmas('MerryMerry'));
// console.log(merryChristmas('ChristmasChristmas'));
// console.log(merryChristmas('MMeerrrryyCChhrriissttmmaass'));
// console.log(merryChristmas('MMmmeerrrrrryyCChhiissssttaa'));
// console.log(merryChristmas('MMmmeerrrryyCChhiissssssttaa'));