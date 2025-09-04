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

// console.log(isPrime(0));
// console.log(isPrime(1));
// console.log(isPrime(2));
// console.log(isPrime(3));
// console.log(isPrime(4));
// console.log(isPrime(5));

// console.log(getPrimes(0, 0));
// console.log(getPrimes(0, 30));
// console.log(getPrimes(30, 0));