function validatePIN(pin) {
    return pin.match(/^(\d{4}|\d{6})$/g) !== null;
}

// console.log(validatePIN('1234'));
// console.log(validatePIN('12345'));
// console.log(validatePIN('a234'));