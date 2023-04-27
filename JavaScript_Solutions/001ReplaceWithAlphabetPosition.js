function alphabetPosition(text) {
    return text.toLowerCase().split('').
        filter(c => c.charCodeAt(0) >= 97 && c.charCodeAt(0) <= 122).
        map(c => c.charCodeAt(0) - 96).
        join(' ');
}

// console.log(alphabetPosition("The sunset sets at twelve o' clock."));
// console.log(alphabetPosition("The narwhal bacons at midnight."));