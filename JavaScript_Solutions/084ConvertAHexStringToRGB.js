function hexStringToRGB(hexString) {
    const result = { r: 0, g: 0, b: 0 };
    const hexToDecimal = (num) => parseInt(num, 16);

    for (let i = 1; i < hexString.length; i += 2) {
        const decimalNum = hexToDecimal(hexString.slice(i, i + 2));

        switch (i) {
            case 1:
                result.r = decimalNum;
                break;
            case 3:
                result.g = decimalNum;
                break;
            case 5:
                result.b = decimalNum;
                break;
        }
    }

    return result;
}

// console.log(hexStringToRGB('#FF9933'));
// console.log(hexStringToRGB('#beaded'));
// console.log(hexStringToRGB('#000000'));
// console.log(hexStringToRGB('#111111'));
// console.log(hexStringToRGB('#Fa3456'));