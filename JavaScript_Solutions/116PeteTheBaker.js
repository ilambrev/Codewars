function cakes(recipe, available) {
    let cakes = 0;

    const reciepeProducts = Object.keys(recipe);

    for (let i = 0; i < reciepeProducts.length; i++) {
        let productAvailableQuantity = 0;
        if (available.hasOwnProperty(reciepeProducts[i])) {
            productAvailableQuantity = available[reciepeProducts[i]];
        }

        let portions = Math.floor(productAvailableQuantity / recipe[reciepeProducts[i]]);

        if (i == 0 || portions < cakes) {
            cakes = portions;
        }
    }

    return cakes;
}

// console.log(cakes({ flour: 500, sugar: 200, eggs: 1 }, { flour: 1200, sugar: 1200, eggs: 5, milk: 200 }));
// console.log(cakes({ apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100 }, { sugar: 500, flour: 2000, milk: 2000 }));