function nextSmaller(n) {
    let numberDigits = n.toString().split('').map(Number);

    for (let i = numberDigits.length - 1; i > 0; i--) {

        let isNumFound = false;

        for (let j = i; j > 0; j--) {

            if (numberDigits[i] < numberDigits[j - 1]) {
                const buffer = numberDigits[j - 1];
                numberDigits[j - 1] = numberDigits[i];
                numberDigits[i] = buffer;

                numberDigits = numberDigits.slice(0, j).concat(numberDigits.slice(j).sort((d1, d2) => d2 - d1));

                isNumFound = true;

                break;
            }

            if (numberDigits[j - 1] < numberDigits[j - 2] && j - 2 > 0 && numberDigits[j - 2] <= numberDigits[i]) {
                break;
            }
        }

        if (isNumFound) {
            break;
        }
    }

    if (numberDigits[0] > 0) {
        const newNumber = Number(numberDigits.join(''));

        if (newNumber < n) {
            return newNumber;
        }

    }

    return -1;
}

// console.log(nextSmaller(21)); // 12
// console.log(nextSmaller(531)); // 513
// console.log(nextSmaller(2071)); // 2017
// console.log(nextSmaller(9)); // -1
// console.log(nextSmaller(111)); // -1
// console.log(nextSmaller(135)); // -1
// console.log(nextSmaller(1027)); // -1
// console.log(nextSmaller(907)); // 790
// console.log(nextSmaller(1234567908)); // 1234567890
// console.log(nextSmaller(513)); // 351
// console.log(nextSmaller(18411328407)); // 18411328074
// console.log(nextSmaller(36189445)); // 36185944
// console.log(nextSmaller(74134)); //73441