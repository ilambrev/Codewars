function generateHashtag(str) {
    let result = str.trim();

    if (result !== '') {
        result = '#' + result
            .split(/\s+/).map(s => {
                s.toLowerCase();
                s = s.charAt(0).toUpperCase() + s.slice(1);

                return s;
            })
            .join('');

        return result.length > 140 ? false : result;
    }

    return false;
}

// console.log(generateHashtag(' Hello there thanks for trying my Kata'));
// console.log(generateHashtag('    Hello     World   '));
// console.log(generateHashtag(''));