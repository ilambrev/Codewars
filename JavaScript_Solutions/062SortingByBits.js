function sortByBit(arr) {

    function compareNums(n1, n2) {
        const n1Bits = countNumBits(n1);
        const n2Bits = countNumBits(n2);
        if (n1Bits - n2Bits < 0) {
            return -1;
        } else if (n1Bits - n2Bits > 0) {
            return 1;
        } else {
            if (n1 - n2 < 0) {
                return -1;
            } else if (n1 - n2 > 0) {
                return 1;
            } else {
                return 0;
            }
        }
    }

    function countNumBits(n) {
        return n.toString(2).split('').filter(d => d == '1').length;
    }

    return arr.sort((n1, n2) => compareNums(n1, n2));
}

// console.log(sortByBit([7, 6, 15, 8]));
// console.log(sortByBit([3, 8, 3, 6, 5, 7, 9, 1]));