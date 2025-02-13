function stockList(books, categories) {
    if (books.length == 0 || categories.length == 0) {
        return '';
    }
    const labels = {};

    for (let book of books) {
        let [label, quantity] = book.split(' ');
        label = label.charAt(0);
        quantity = Number(quantity);

        if (!labels.hasOwnProperty(label)) {
            labels[label] = 0;
        }

        labels[label] += quantity;
    }

    return categories.map(c => `(${c} : ${labels.hasOwnProperty(c) ? labels[c] : 0})`).join(' - ');
}

// console.log(stockList(
//     ['ABART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60'],
//     ['A', 'B', 'C', 'W']
// ));
// console.log(stockList(
//     ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600'],
//     ['A', 'B', 'C', 'D']
// ));
// console.log(stockList(
//     ['ABAR 200', 'CDXE 500', 'BKWR 250', 'BTSQ 890', 'DRTY 600'],
//     ['A', 'B']
// ));