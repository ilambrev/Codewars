function encode(string) {
    const vowelValues = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5,
    }

    const encodedString = string.split('').map(l => {
        if (vowelValues.hasOwnProperty(l)) {
            return vowelValues[l];
        }

        return l;
    }).join('');

    return encodedString;
}

function decode(string) {
    const vowelValues = {
        1: 'a',
        2: 'e',
        3: 'i',
        4: 'o',
        5: 'u',
    }

    const decodedString = string.split('').map(l => {
        if (vowelValues.hasOwnProperty(l)) {
            return vowelValues[l];
        }

        return l;
    }).join('');

    return decodedString;
}

// console.log(encode('hello'));
// console.log(decode('h3 th2r2'));