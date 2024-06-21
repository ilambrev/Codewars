function findUniq(arr) {
    const letters = new Set();

    let string = arr[0].toLowerCase();

    for (let i = 0; i < string.length; i++) {
        if (string.charAt(i) !== ' ') {
            letters.add(string.charAt(i));
        }
    }

    string = arr[1].toLowerCase();

    let isStringWithSimilarLetters = true;

    for (let i = 0; i < string.length; i++) {
        if (string.charAt(i) !== ' ' && !letters.has(string.charAt(i))) {
            isStringWithSimilarLetters = false;
            break;
        }
    }

    if (!isStringWithSimilarLetters) {
        string = arr[2].toLowerCase();

        for (let i = 0; i < string.length; i++) {
            if (string.charAt(i) !== ' ' && !letters.has(string.charAt(i))) {
                return arr[0];
            }
        }

        return arr[1];
    }

    for (let i = 2; i < arr.length; i++) {
        string = arr[i].toLowerCase();

        for (let j = 0; j < string.length; j++) {
            if (string.charAt(j) !== ' ' && !letters.has(string.charAt(j))) {
                return arr[i];
            }
        }
    }

    return arr.filter(s => s.trim() === '')[0];
}

// console.log(findUniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']));
// console.log(findUniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']));