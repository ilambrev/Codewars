function rgb(r, g, b) {
    const decimalToHex = (num) => {
        if (num < 0) {
            num = 0;
        }
        if (num > 255) {
            num = 255;
        }
        return num < 16 ? '0' + num.toString(16) : num.toString(16);
    }

    return (decimalToHex(r) + decimalToHex(g) + decimalToHex(b)).toUpperCase();
}

// console.log(rgb(0, 0, 0));
// console.log(rgb(0, 0, -20));
// console.log(rgb(300, 255, 255));
// console.log(rgb(173, 255, 47));