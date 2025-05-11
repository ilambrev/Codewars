function isAlt(word) {
    const vovels = new Set(['a', 'e', 'i', 'o', 'u']);
    const isFirstLetterVowel = vovels.has(word.charAt(0));

    if (isFirstLetterVowel) {
        for (let i = 0; i < word.length; i++) {
            if (i % 2 == 0 && !vovels.has(word.charAt(i))) {
                return false;
            }
            if (i % 2 != 0 && vovels.has(word.charAt(i))) {
                return false;
            }
        }
    } else {
        for (let i = 0; i < word.length; i++) {
            if (i % 2 == 0 && vovels.has(word.charAt(i))) {
                return false;
            }
            if (i % 2 != 0 && !vovels.has(word.charAt(i))) {
                return false;
            }
        }
    }

    return true;
}

// console.log(isAlt('amazon'));
// console.log(isAlt('apple'));
// console.log(isAlt('banana'));