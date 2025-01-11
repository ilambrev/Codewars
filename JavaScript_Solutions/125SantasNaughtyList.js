function findChildren(santasList, children) {
    return Object.keys(children.reduce((acc, curr) => {
        if (santasList.indexOf(curr) > -1) {
            acc[curr] = true;
        }
        return acc;
    }, {})).sort();
}

// console.log(findChildren(['Jason', 'Jackson', 'Jordan', 'Johnny'], ['Jason', 'Jordan', 'Jennifer']));
// console.log(findChildren(['jASon', 'JAsoN', 'JaSON', 'jasON'], ['JasoN', 'jASOn', 'JAsoN', 'jASon', 'JASON']));
// console.log(findChildren(['Jason', 'James', 'Johnson'], ['Jason', 'James', 'JJ']));