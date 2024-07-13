function toUnderscore(string) {
    if (typeof string != 'string') {
        return string.toString();
    }

    const result = string.split('').reduce((acc, curr, i) => {
        if (curr >= 'A' && curr <= 'Z') {
            curr = curr.toLowerCase();
            if (i > 0) {
                acc.push('_');
            }
        }

        acc.push(curr);
        return acc;
    }, []);

    return result.join('');
}

// console.log(toUnderscore('TestController'));
// console.log(toUnderscore('MoviesAndBooks'));
// console.log(toUnderscore('App7Test'));
// console.log(toUnderscore(1));