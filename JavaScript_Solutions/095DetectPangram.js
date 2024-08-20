function isPangram(string) {
    const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

    string = string.toLowerCase();

    for (let letter of alphabet) {
        if (!string.includes(letter)) {
            return false;
        }
    }

    return true;
}

// console.log(isPangram("The quick brown fox jumps over the lazy dog."));
// console.log(isPangram("This is not a pangram."));