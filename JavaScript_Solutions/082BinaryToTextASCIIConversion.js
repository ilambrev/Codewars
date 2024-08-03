function binaryToString(binary) {
    const nums = [];

    for (let i = 0; i < binary.length; i += 8) {
        const decimalNum = Number('0b' + binary.slice(i, i + 8));
        nums.push(decimalNum);
    }

    return nums ? String.fromCharCode(...nums) : '';
}

// console.log(binaryToString('01100001'));
// console.log(binaryToString('01001011010101000100100001011000010000100101100101000101'));
// console.log(binaryToString('00110001001100000011000100110001'));
// console.log(binaryToString('001111000011101000101001'));
// console.log(binaryToString(''));