function validISBN10(isbn) {
    const isbnElements = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'X': 10
    }

    if (isbn.length != 10) {
        return false;
    }

    if (isbn.indexOf('X') > -1 && isbn.indexOf('X') != 9) {
        return false;
    }

    let sum = 0;

    for (let i = 0; i < isbn.length; i++) {
        if (!isbnElements.hasOwnProperty(isbn.charAt(i))) {
            return false;
        }
        sum += isbnElements[isbn.charAt(i)] * (i + 1);
    }

    return sum % 11 == 0;
}

// console.log(validISBN10('1112223339'));
// console.log(validISBN10('111222333'));
// console.log(validISBN10('1112223339X'));
// console.log(validISBN10('1234554321'));
// console.log(validISBN10('1234512345'));
// console.log(validISBN10('048665088X'));
// console.log(validISBN10('X123456788'));