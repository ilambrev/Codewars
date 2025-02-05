function findMissingLetter(array) {
    let missingLetter = '';
    for (let i = 0; i < array.length - 1; i++) {
        const nextLetter = String.fromCharCode(array[i].charCodeAt(0) + 1);
        if (array[i + 1] !== nextLetter) {
            missingLetter = nextLetter;
            break;
        }
    }
    return missingLetter;
}

// console.log(findMissingLetter(['a', 'b', 'c', 'd', 'f']));
// console.log(findMissingLetter(['O', 'Q', 'R', 'S']));