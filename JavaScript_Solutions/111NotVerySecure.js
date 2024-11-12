function alphanumeric(string) {
    const pattern = /^[a-zA-Z0-9]+$/g;

    return pattern.test(string);
}

// console.log(alphanumeric('Mazinkaiser'));
// console.log(alphanumeric('hello world_'));
// console.log(alphanumeric('PassW0rd'));
// console.log(alphanumeric('     '));