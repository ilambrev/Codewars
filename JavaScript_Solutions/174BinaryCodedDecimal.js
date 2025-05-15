function toBcd(number) {
    const decimalToBinary = {
        0: '0000',
        1: '0001',
        2: '0010',
        3: '0011',
        4: '0100',
        5: '0101',
        6: '0110',
        7: '0111',
        8: '1000',
        9: '1001',
    }
    const digits = String(Math.abs(number)).split('').map(Number);
    let result = digits.map(d => decimalToBinary[d]).join(' ');
    if (number < 0) {
        result = '-' + result;
    }

    return result;
}

// console.log(toBcd(10));
// console.log(toBcd(-10));