function theBiggestSearchKeys() {
    if (arguments.length == 0) {
        return "''";
    }

    let result = [];
    for (let i = 0; i < arguments.length; i++) {
        result.push(arguments[i]);
    }

    result.sort((a1, a2) => a2.length - a1.length);

    return `${result
        .filter(a => a.length == result[0].length)
        .sort()
        .map(a => `'${a}'`)
        .join(', ')}`;
}

// console.log(theBiggestSearchKeys('key1', 'key2', 'key3', 'key n', 'bigkey2', 'bigkey1'));
// console.log(theBiggestSearchKeys('key1', 'key22', 'key333'));
// console.log(theBiggestSearchKeys('coding', 'sorting', 'tryruby'));
// console.log(theBiggestSearchKeys('small keyword', 'how to coding?', 'very nice kata', 'a lot of keys', 'I like Ruby!!!'));
// console.log(theBiggestSearchKeys('pippi'));
// console.log(theBiggestSearchKeys());