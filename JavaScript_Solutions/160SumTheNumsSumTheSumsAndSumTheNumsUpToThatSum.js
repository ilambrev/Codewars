function sumOfSums(n) {
    let z = BigInt(n) * (BigInt(n) + BigInt(1)) * (BigInt(n) + BigInt(2)) / BigInt(6);
    let s = z * (z + BigInt(1)) / BigInt(2);

    return s;
}

// console.log(sumOfSums(3));
// console.log(sumOfSums(5));
// console.log(sumOfSums(100));