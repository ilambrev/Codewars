function exchangeWith(a, b) {
    a.reverse();
    b.reverse();

    const reversedArrayA = a.reduce((acc, curr) => {
        acc.push(curr);

        return acc;
    }, []);
    const reversedArrayB = b.reduce((acc, curr) => {
        acc.push(curr);

        return acc;
    }, []);

    a.length = 0;
    b.length = 0;

    for (let element of reversedArrayB) {
        a.push(element);
    }

    for (let element of reversedArrayA) {
        b.push(element);
    }
}

// exchangeWith(['a', 'b', 'c'], [1, 2, 3]);
// exchangeWith(['1', '2', '3', '4', '5', '6', '7'], ['a', 'b', 'c']);