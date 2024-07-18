function revrot(str, sz) {
    const chunks = [];

    if (str.length == '' || sz <= 0 || str.length < sz) {
        return '';
    }

    for (let i = 0; i < str.length; i += sz) {
        const chunk = str.slice(i, i + sz);

        if (chunk.length == sz) {
            chunks.push(chunk);
        }
    }

    for (let i = 0; i < chunks.length; i++) {
        const chunckDigitsSum = chunks[i].split('').map(Number).reduce((acc, curr) => acc += curr, 0);

        if (chunckDigitsSum % 2 == 0) {
            chunks[i] = chunks[i].split('').reverse().join('');
        } else {
            chunks[i] = chunks[i].slice(1, chunks[i].length) + chunks[i].charAt(0);
        }
    }

    return chunks.join('');
}

// console.log(revrot('123456987654', 6));
// console.log(revrot('123456987653', 6));
// console.log(revrot('66443875', 4));
// console.log(revrot('66443875', 8));
// console.log(revrot('664438769', 8));
// console.log(revrot('123456779', 8));
// console.log(revrot('', 8));
// console.log(revrot('123456779', 0));
// console.log(revrot('563000655734469485', 4));