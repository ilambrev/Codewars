function sortTheInnerContent(words) {
    return words.split(' ').map(w => {
        if (w.length > 2) {
            const letters = w.split('');
            const sortedWord =
                letters[0] +
                letters
                    .slice(1, letters.length - 1)
                    .sort((l1, l2) => l2.localeCompare(l1)).join('') +
                letters[letters.length - 1];
            return sortedWord;
        }
        return w;
    }).join(' ');
}

// console.log(sortTheInnerContent('sort the inner content in descending order'));
// console.log(sortTheInnerContent('wait for me'));
// console.log(sortTheInnerContent('this kata is easy'));