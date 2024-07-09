function winner(deckSteve, deckJosh) {
    const moves = deckSteve.length;
    let steavePoints = 0;
    let joshPoints = 0;
    const cards = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    };

    for (let i = 0; i < moves; i++) {
        if (cards[deckSteve[i]] > cards[deckJosh[i]]) {
            steavePoints++;
        } else if (cards[deckSteve[i]] < cards[deckJosh[i]]) {
            joshPoints++;
        }
    }

    if (steavePoints > joshPoints) {
        return `Steve wins ${steavePoints} to ${joshPoints}`;
    } else if (steavePoints < joshPoints) {
        return `Josh wins ${joshPoints} to ${steavePoints}`;
    } else {
        return `Tie`;
    }
}

// console.log(winner(['A', '7', '8'], ['K', '5', '9']));