function printerError(s) {
    const controlStringLength = s.length;
    const errors = s.split('').filter(c => c < 'a' || c > 'm').length;

    return `${errors}/${controlStringLength}`;
}

// console.log(printerError('aaabbbbhaijjjm'));
// console.log(printerError('aaaxbbbbyyhwawiwjjjwwm'));
// console.log(printerError('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'));