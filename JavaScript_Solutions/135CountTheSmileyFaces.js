function countSmileys(arr) {
    const validSmiley = new Set([
        ':)', ':-)', ':~)',
        ';)', ';-)', ';~)',
        ':D', ':-D', ':~D',
        ';D', ';-D', ';~D'
    ]);

    return arr.filter(s => validSmiley.has(s)).length;
}

// console.log(countSmileys([]));
// console.log(countSmileys([':D', ':~)', ';~D', ':)']));
// console.log(countSmileys([':)', ':(', ':D', ':O', ':;']));
// console.log(countSmileys([';]', ':[', ';*', ':$', ';-D']));