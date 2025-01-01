function sortPoker(john, uncle) {
    const cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
    const suits = [
        { 'type': '♠', 'index': -1 },
        { 'type': '♥', 'index': -1 },
        { 'type': '♦', 'index': -1 },
        { 'type': '♣', 'index': -1 }
    ];

    for (let suit of suits) {
        suit.index = uncle.indexOf(suit.type);
    }

    suits.sort((s1, s2) => s1.index - s2.index);

    const johnSuits = [];

    for (let suit of suits) {
        for (let card of cards) {
            let i = 0;
            while (i < john.length) {
                let matchIndex = john.indexOf(suit.type + card, i);
                if (matchIndex > -1) {
                    johnSuits.push(suit.type + card);
                    i = matchIndex + 1;
                } else {
                    break;
                }
            }
        }
    }

    return johnSuits.join('');
}

// console.log(sortPoker('♦6♥2♠3♦5♠J♣Q♠K♣7♦2♣5♥5♥10♠A', '♠2♠3♠5♥J♥Q♥K♣8♣9♣10♦4♦5♦6♦7'));
// console.log(sortPoker('♦6♥2♠3♦5♠J♣Q♠K♣7♦2♣5♥5♥10♠A', '♣8♣9♣10♦4♦5♦6♦7♠2♠3♠5♥J♥Q♥K'));
// console.log(sortPoker('♣10♠10♦A♥Q♥K♣2♠5♦6♣K♦6♦4♦4♦J', '♣8♣10♣A♣A♠3♠4♠6♦8♦J♦K♥9♥A♥A'));