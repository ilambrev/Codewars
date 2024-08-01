function insideOut(x) {
    const words = x.split(' ');

    function reverse(word) {
        const n = word.length;
        const wordAsArr = word.split('');
        let leftSide = wordAsArr.slice(0, n / 2).reverse().join('');
        let rightSide = '';
        let middle = '';

        if (n % 2 != 0) {
            const middleIndex = Math.floor(n / 2);
            rightSide = wordAsArr.slice(middleIndex + 1).reverse().join('')
            middle = wordAsArr[middleIndex];
        } else {
            rightSide = wordAsArr.slice(n / 2).reverse().join('');
        }

        return leftSide + middle + rightSide;
    }

    return words.map(reverse).join(' ');
}

// console.log(insideOut('taxi'));
// console.log(insideOut('taxis'));