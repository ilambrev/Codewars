function XO(str) {
    const symbolsArr = str.split('');
    const xCount = symbolsArr.filter(s => s.toLowerCase() === 'x').length;
    const oCount = symbolsArr.filter(s => s.toLowerCase() === 'o').length;

    return xCount === oCount;
}

// console.log(XO("ooxx"));
// console.log(XO("xooxx"));
// console.log(XO("ooxXm"));
// console.log(XO("zpzpzpp"));
// console.log(XO("zzoo"));