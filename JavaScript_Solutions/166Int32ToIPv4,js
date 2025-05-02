function int32ToIp(int32) {
    let binaryRep = [];

    for (let i = 31; i >= 0; i--) {
        const powerOfTwo = Math.pow(2, i);
        if (int32 >= powerOfTwo) {
            binaryRep.push('1');
            int32 -= powerOfTwo;
        } else {
            binaryRep.push('0');
        }
    }

    const octets = [];

    for (let i = 0; i < binaryRep.length; i += 8) {
        octets.push(parseInt(binaryRep.slice(i, i + 8).join(''), 2).toString(10));
    }

    return octets.join('.');
}

// console.log(int32ToIp(2149583361));
// console.log(int32ToIp(32));
// console.log(int32ToIp(0));
// console.log(int32ToIp(2154959208));
// console.log(int32ToIp(2 ** 32 - 1));