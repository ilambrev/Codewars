function sortString(string, ordering) {
    const result = new Map();

    for (let i = 0; i < ordering.length; i++) {
        if (!result.has(ordering.charAt(i))) {
            result.set(ordering.charAt(i), 0);
        }
    }

    let unmachedChars = '';

    for (let i = 0; i < string.length; i++) {
        const currentChar = string.charAt(i);
        if (result.has(currentChar)) {
            let count = result.get(currentChar);
            result.set(currentChar, count += 1);
        } else {
            unmachedChars += currentChar;
        }
    }

    return Array.from(result).map(([k, v]) => k.repeat(v)).join('') + unmachedChars;
}

// console.log(sortString('foos', 'of'));
// console.log(sortString('string', 'gnirts'));
// console.log(sortString('banana', 'abn'));