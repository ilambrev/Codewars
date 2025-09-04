function isPrime(number) {
    isNumberPrime = number > 1

    for (let i = 2; i < number; i++) {
        if (number % i == 0) {
            isNumberPrime = false;
            break;
        }
    }

    return isNumberPrime;
}

function getPrimes(start, finish) {
    const primeNumbers = [];

    minValue = Math.min(start, finish);
    maxValue = Math.max(start, finish);

    if (minValue < 2) {
        minValue == 2;
    }

    for (let i = minValue; i <= maxValue; i++) {
        if (isPrime(i)) {
            primeNumbers.push(i);
        }
    }

    return primeNumbers;
}

// console.log(isPrime(0)); // false
// console.log(isPrime(1)); // false
// console.log(isPrime(2)); // true
// console.log(isPrime(3)); // true
// console.log(isPrime(4)); // false
// console.log(isPrime(5)); // true

// console.log(getPrimes(0, 0)); // []
// console.log(getPrimes(0, 30)); // [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
// console.log(getPrimes(30, 0)); // [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]