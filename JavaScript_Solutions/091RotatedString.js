function isRotation(s1, s2) {
    if (s1.length != s2.length) {
        return false;
    }

    if (s1 == '' && s2 == '') {
        return true;
    }

    const stringAsArray = s1.split('');

    for (let i = 0; i < s1.length; i++) {
        if (stringAsArray.join('') === s2) {
            return true;
        }
        const firstElement = stringAsArray.shift();
        stringAsArray.push(firstElement);
    }

    return false;
}

// console.log(isRotation('hello', 'ohell'));
// console.log(isRotation('hello', 'lloeh'));