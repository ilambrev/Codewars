const children = new Set();

function handOutGift(name) {
    if (children.has(name)) {
        throw new Error('${name} tries to get two gifts!');
    } else {
        children.add(name);
    }
}

// handOutGift('Peter');
// handOutGift('Alison');
// handOutGift('John');
// handOutGift('Maria');
// handOutGift('Peter');