function validPhoneNumber(phoneNumber) {
    const regexp = /^\(\d{3}\) \d{3}-\d{4}$/;

    return regexp.test(phoneNumber);
}

// console.log(validPhoneNumber('(123) 456-7890'));
// console.log(validPhoneNumber('(1111)555 2345'));
// console.log(validPhoneNumber('(098) 123 4567'));