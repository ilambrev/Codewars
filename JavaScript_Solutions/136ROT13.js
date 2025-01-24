function rot13(str) {
    const letters = [];

    for (let i = 0; i < str.length; i++) {
        let letterCode = str.charCodeAt(i);
        if (letterCode >= 65 && letterCode <= 90) {
            letterCode = 90 - letterCode >= 13 ? letterCode + 13 : 64 + 13 - (90 - letterCode);
        } else if (letterCode >= 97 && letterCode <= 122) {
            letterCode = 122 - letterCode >= 13 ? letterCode + 13 : 96 + 13 - (122 - letterCode);
        }
        letters.push(String.fromCharCode(letterCode));
    }

    return letters.join('');
}

// console.log(rot13('EBG13 rknzcyr.'));
// console.log(rot13('This is my first ROT13 excercise!'));