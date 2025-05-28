function findNb(m) {
    let n = 0;
    while (m > 0) {
        n++;
        m -= Math.pow(n, 3);
    }
    return m == 0 ? n : -1;
}

// console.log(findNb(1071225));
// console.log(findNb(91716553919377));
// console.log(findNb(4183059834009));
// console.log(findNb(24723578342962));
// console.log(findNb(135440716410000));
// console.log(findNb(40539911473216));