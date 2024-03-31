function expandedForm(num) {

    return num.toString().split('')
        .map((d, i) => d !== '0' ? d + '0'.repeat(num.toString().length - 1 - i) : '0')
        .filter(d => d !== '0')
        .join(' + ');

}

// console.log(expandedForm(70304));