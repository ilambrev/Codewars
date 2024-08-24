function expandedForm(num) {
    let [integerPart, fractionalPart] = num.toString().split('.');

    const result = [];

    for (let i = 0; i < integerPart.length; i++) {
        const num = Number(integerPart.charAt(i));
        if (num > 0) {
            result.push(num * Math.pow(10, integerPart.length - 1 - i));
        }
    }

    for (let i = 0; i < fractionalPart.length; i++) {
        const num = Number(fractionalPart.charAt(i));
        if (num > 0) {
            result.push(`${num}/${Math.pow(10, i + 1)}`);
        }
    }

    return result.join(' + ');
}

// console.log(expandedForm(807.304)); //Should return "800 + 7 + 3/10 + 4/1000"
// console.log(expandedForm(1.24)); //Should return "1 + 2/10 + 4/100"
// console.log(expandedForm(7.304)); //Should return "7 + 3/10 + 4/1000"
// console.log(expandedForm(0.04)); //Should return "4/100"