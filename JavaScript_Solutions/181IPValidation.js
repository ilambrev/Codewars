function isValidIP(str) {
    const regexp = /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/;

    if (str.match(regexp)) {
        const octets = str.split('.');

        for (let i = 0; i < octets.length; i++) {
            if (octets[i].length > 1 && octets[i].charAt(0) == '0') {
                return false;
            }

            const octetValue = Number(octets[i]);

            if (octetValue > 255) {
                return false;
            }
        }

        return true;
    }

    return false;
}

// console.log(isValidIP('0.0.0.0'));
// console.log(isValidIP('12.255.56.1'));
// console.log(isValidIP('137.255.156.100'));
// console.log(isValidIP(''));
// console.log(isValidIP('abc.def.ghi.jkl'));
// console.log(isValidIP('123.456.789.0'));
// console.log(isValidIP('12.34.56'));
// console.log(isValidIP('01.02.03.04'));
// console.log(isValidIP('256.1.2.3'));
// console.log(isValidIP('1.2.3.4.5'));
// console.log(isValidIP('123,45,67,89'));
// console.log(isValidIP('1e0.1e1.1e2.2e2'));
// console.log(isValidIP(' 1.2.3.4'));
// console.log(isValidIP('1.2.3.4 '));
// console.log(isValidIP('12.34.56.-7'));
// console.log(isValidIP('1.2.3.4\n'));
// console.log(isValidIP('\n1.2.3.4'));
// console.log(isValidIP('1.2.3.4'));
// console.log(isValidIP('123.45.67.89'));
// console.log(isValidIP('1.2.3'));
// console.log(isValidIP('1.2.3.4.5'));
// console.log(isValidIP('123.456.78.90'));
// console.log(isValidIP('123.045.067.089'));