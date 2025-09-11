deck = ["joker", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣",
        "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
        "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
        "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]

def card_game(card_1, card_2, trump):
    if card_1 == card_2:
        return 'Someone cheats.'
    elif card_1 == 'joker' or (card_1[-1] == trump and card_2[-1] != trump):
        return 'The first card won.'
    elif card_2 == 'joker' or (card_1[-1] != trump and card_2[-1] == trump):
        return 'The second card won.'
    elif card_1[-1] == card_2[-1]:
        return 'The first card won.' if deck.index(card_1) > deck.index(card_2) else 'The second card won.'
    else:
        return 'Let us play again.'

# print(card_game("Q♣", "3♣", "♦"))
# print(card_game("3♣", "Q♣", "♦"))
# print(card_game("5♥", "A♣", "♦"))
# print(card_game("8♠", "8♠", "♣"))
# print(card_game("2♦", "A♠", "♦"))
# print(card_game("A♠", "2♦", "♦"))
# print(card_game("joker", "joker", "♦"))
# print(card_game("joker", "10♣", "♠"))
# print(card_game("10♣", "joker", "♠"))