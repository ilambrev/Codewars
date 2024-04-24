function digitalRoot(n) {
    let root = n;
    let digits = root.toString().split('');

    while (digits.length > 1) {
        root = digits.map(Number).reduce((acc, curr) => acc + curr, 0);

        digits = root.toString().split('');
    }

    return root;
}

// console.log(digitalRoot(16));
// console.log(digitalRoot(942));
// console.log(digitalRoot(132189));
// console.log(digitalRoot(493193));