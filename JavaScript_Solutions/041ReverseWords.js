function reverseWords(str) {
    return str
        .split(/(\s+)/)
        .map(w => w.split('').reverse().join(''))
        .join('');
}

// console.log(reverseWords('This is an example!'));
// console.log(reverseWords('double  spaces'));