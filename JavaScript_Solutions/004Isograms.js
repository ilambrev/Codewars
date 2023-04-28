function isIsogram(str) {

    let strLowerCase = str.toLowerCase();
    let letters = [];
    let isIsogram = true;

    for (let i = 0; i < strLowerCase.length; i++) {

        let letter = strLowerCase.charAt(i);

        if (letters.includes(letter)) {

            isIsogram = false;
            break;

        } else {

            letters.push(letter);

        }

    }

    return isIsogram;
}

// console.log(isIsogram("Dermatoglyphics"));
// console.log(isIsogram("moose"));
// console.log(isIsogram("aba"));
// console.log(isIsogram("isogram"));
// console.log(isIsogram("moOse"));
// console.log(isIsogram("isIsogram"));
// console.log(isIsogram(""));