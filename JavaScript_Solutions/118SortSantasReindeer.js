function sortReindeer(reindeerNames) {
    reindeerNames.sort((n1, n2) => n1.split(' ')[1].localeCompare(n2.split(' ')[1]));

    return reindeerNames;
}

// console.log(sortReindeer([
//     'Dasher Tonoyan',
//     'Dancer Moore',
//     'Prancer Chua',
//     'Vixen Hall',
//     'Comet Karavani',
//     'Cupid Foroutan',
//     'Donder Jonker',
//     'Blitzen Claus'
// ]));