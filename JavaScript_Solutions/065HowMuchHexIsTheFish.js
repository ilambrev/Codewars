function fisHex(name) {
    const hexSymbols = {
        a: 10,
        b: 11,
        c: 12,
        d: 13,
        e: 14,
        f: 15,
    }

    const result = name.toLowerCase()
        .split('')
        .reduce((acc, curr) => {
            if (hexSymbols.hasOwnProperty(curr)) {
                acc = acc ^ hexSymbols[curr];
            }
            return acc;
        }, 0);

    return result;
}

// console.log(fisHex('redlionfish'));
// console.log(fisHex('pufferfish'));
// console.log(fisHex('puffers'));
// console.log(fisHex('balloonfish'));
// console.log(fisHex('blowfish'));
// console.log(fisHex('bubblefish'));
// console.log(fisHex('globefish'));
// console.log(fisHex('swellfish'));
// console.log(fisHex('toadfish'));
// console.log(fisHex('toadies'));
// console.log(fisHex('honey toads'));
// console.log(fisHex('sugar toads'));
// console.log(fisHex('sea squab'));