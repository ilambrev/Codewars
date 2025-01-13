function shoppingCalculation(input) {
    const products = {};
    const customers = [];
    const purchases = [];

    for (let line of input) {
        line = line.substring(0, line.length - 1);
        let lineContent = line.split(' ');
        switch (lineContent[1]) {
            case 'is':
                products[lineContent[0].toLowerCase()] = Number(lineContent[2].substring(1));
                break;
            case 'has':
                customers.push({ name: lineContent[0], money: Number(lineContent[2].substring(1)), purchases: [] });
                break;
            case 'buys':
                let product = lineContent[3];
                if (product.charAt(product.length - 1) == 's') {
                    product = product.substring(0, product.length - 1);
                }
                purchases.push({ customer: lineContent[0], quantity: Number(lineContent[2]), product: product });
                break;
        }
    }

    for (let purchase of purchases) {
        const customerIndex = customers.findIndex(c => c.name === purchase.customer);
        const purchasePrice = purchase.quantity * (products[purchase.product]);
        customers[customerIndex].money -= purchasePrice;
        customers[customerIndex].purchases.push({ product: purchase.product, quantity: purchase.quantity });
    }

    return customers.map(c => [c.name, '$' + c.money, c.purchases
        .map(p => p.quantity + ' ' + (p.quantity > 1 ? p.product + 's' : p.product)).join(', ')]);
}

// console.log(shoppingCalculation([
//     'Apple is $5.',
//     'Banana is $7.',
//     'Orange is $2.',
//     'Alice has $26.',
//     'John has $41.',
//     'Alice buys 2 apples.',
//     'John buys 1 banana.',
//     'Alice buys 5 oranges.'
// ]));
// console.log(shoppingCalculation([
//     'Chocolate is $15.',
//     'George has $100.',
//     'Ross has $80.',
//     'George buys 5 chocolates.',
//     'Ross buys 1 chocolate.',
// ]));
// console.log(shoppingCalculation([
//     'Carrot is $1.',
//     'Watermelon is $5.',
//     'Lemon is $2.',
//     'Steve has $10.',
//     'Jim has $800.',
//     'Steve buys 7 carrots.',
//     'Jim buys 2 watermelons.',
//     'Jim buys 1 carrot.'
// ]));
// console.log(shoppingCalculation([
//     'Carrot is $1.',
//     'Jim has $10.',
//     'Lemon is $2.',
//     'Steve has $80.',
//     'Steve buys 7 carrots.',
//     'Jim buys 2 lemons.',
// ]));
// console.log(shoppingCalculation([
//     'Apple is $5.',
//     'Banana is $7.',
//     'Orange is $2.',
//     'Lisa has $26.',
//     'Arthas has $41.',
//     'Lisa buys 2 apples.',
//     'Arthas buys 1 banana.',
//     'Lisa buys 5 oranges.',
// ]));