function spinWords(string) {
    const wordLength = 5;

    const result = string.split(/\s+/).map(w => {
        if (w.length >= wordLength) {
            w = w.split('').reverse().join('');
        }

        return w;
    }).join(' ');

    return result;
}

// console.log(spinWords('Hey fellow warriors'));
// console.log(spinWords('This is a test'));
// console.log(spinWords('This is another test'));