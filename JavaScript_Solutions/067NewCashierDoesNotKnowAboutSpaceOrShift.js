function getOrder(input) {
    const menu = [
        'Burger',
        'Fries',
        'Chicken',
        'Pizza',
        'Sandwich',
        'Onionrings',
        'Milkshake',
        'Coke',
    ];

    const orders = menu.reduce((acc, curr) => {
        const article = curr.toLowerCase();

        while (input.indexOf(article) != -1) {
            input = input.replace(article, '');
            acc.push(curr);
        }
        return acc;
    }, []);

    return orders.join(' ');
}

// console.log(getOrder('milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza'));
// console.log(getOrder('pizzachickenfriesburgercokemilkshakefriessandwich'));