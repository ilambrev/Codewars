let countBits = function (n) {
    return n.toString(2).split('').filter(s => s == '1').length;
}

// console.log(countBits(1234));
// console.log(countBits(0));
// console.log(countBits(4));
// console.log(countBits(7));
// console.log(countBits(9));
// console.log(countBits(10));