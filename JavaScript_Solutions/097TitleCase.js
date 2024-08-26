function titleCase(title, minorWords) {
    if (!title) {
        return title;
    }

    if (arguments.length == 1 || !minorWords) {
        return title.toLowerCase()
            .split(' ')
            .map(w => w[0].toUpperCase() + w.substring(1)).join(' ');
    }

    if (arguments.length == 2) {
        const minorWordsArr = minorWords.toLowerCase().split(' ');
        return title.toLowerCase()
            .split(' ')
            .map((w, i) => {
                const index = minorWordsArr.indexOf(w);
                if (index == -1 || i == 0) {
                    w = w[0].toUpperCase() + w.substring(1)
                }
                return w;
            }).join(' ');
    }
}

// console.log(titleCase(''));
// console.log(titleCase('a clash of KINGS', ''));
// console.log(titleCase('a clash of KINGS', 'a an the of'));
// console.log(titleCase('THE WIND IN THE WILLOWS', 'The In'));
// console.log(titleCase('the quick brown fox'));