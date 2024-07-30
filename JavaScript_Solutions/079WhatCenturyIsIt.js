function whatCentury(year) {
    const yearsInCentury = 100;
    const century = Math.ceil(Number(year) / yearsInCentury);
    const endings = {
        0: 'th',
        1: 'st',
        2: 'nd',
        3: 'rd',
    }

    const lastDigit = century < 10 ? century : century >= 10 && century < 20 ? 0 : century % 10;

    if (lastDigit < 4) {
        return century + endings[lastDigit];
    } else {
        return century + endings[0];
    }
}

// console.log(whatCentury('1999'));
// console.log(whatCentury('2011'));
// console.log(whatCentury('2154'));
// console.log(whatCentury('2259'));
// console.log(whatCentury('1124'));
// console.log(whatCentury('2000'));