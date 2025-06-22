function broken(x) {
    return x.split('').reduce((acc, curr) => {
        if (curr == '1') {
            acc.push('0')
        } else {
            acc.push('1');
        }
        return acc;
    }, []).join('');
}

// console.log(broken('1'));
// console.log(broken('10000000101101111110011001000'));
// console.log(broken('100010'));