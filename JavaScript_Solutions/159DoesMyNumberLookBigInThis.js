function narcissistic(value) {
    const digits = value.toString().split('').map(Number);

    const sumOfPoweredDigits = digits.reduce((acc, curr) => acc + curr ** digits.length, 0);

    return sumOfPoweredDigits == value;
}

// console.log(narcissistic(7));
// console.log(narcissistic(153));
// console.log(narcissistic(122));
// console.log(narcissistic(487));