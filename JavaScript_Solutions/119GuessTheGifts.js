function guessGifts(wishlist, presents) {
    const presentsThatYouMightHaveGotten = {};

    for (let present of presents) {
        for (let wishlistPresent of wishlist) {
            if (present.size == wishlistPresent.size &&
                present.clatters == wishlistPresent.clatters &&
                present.weight == wishlistPresent.weight) {

                presentsThatYouMightHaveGotten[wishlistPresent.name] = wishlistPresent.name;
            }
        }
    }

    return Object.keys(presentsThatYouMightHaveGotten);
}

// console.log(guessGifts(
//     [
//         { name: "mini puzzle", size: "small", clatters: "yes", weight: "light" },
//         { name: "toy car", size: "medium", clatters: "a bit", weight: "medium" },
//         { name: "card game", size: "small", clatters: "no", weight: "light" }
//     ],
//     [
//         { size: "medium", clatters: "a bit", weight: "medium" },
//         { size: "small", clatters: "yes", weight: "light" }
//     ]
// ));