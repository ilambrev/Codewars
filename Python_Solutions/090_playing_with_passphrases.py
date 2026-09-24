from string import ascii_letters, ascii_lowercase, digits


def play_pass(s, n):
    result = []
    letters_count = len(ascii_lowercase)
    shift = n % letters_count

    for i in range(len(s)):
        symbol = s[i]

        if symbol in ascii_letters:
            shift_index = (ascii_lowercase.index(symbol.lower()) + shift) % letters_count
            symbol = ascii_lowercase[shift_index]
            symbol = symbol.upper() if i % 2 == 0 else symbol.lower()
        elif symbol in digits:
            symbol = str(9 - int(symbol))

        result.append(symbol)

    return "".join(result[::-1])


# print(play_pass("I LOVE YOU!!!", 1))
# print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
# print(play_pass("AAABBCCY", 1))
# print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
# print(play_pass("TO BE HONEST WITH YOU I DON'T USE THIS TEXT TOOL TOO OFTEN BUT HEY... MAYBE YOUR NEEDS ARE DIFFERENT.", 5))
# print(play_pass("IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...", 20))
# print(play_pass("IN 2012 TWO CAMBRIDGE UNIVERSITY RESEARCHERS ANALYSED PASSPHRASES FROM THE AMAZON PAY SYSTEM...", 10))
# print(play_pass("1ONE2TWO3THREE4FOUR5FIVE6SIX7SEVEN8EIGHT9NINE", 5))
# print(play_pass("AZ12345678ZA", 1))
# print(play_pass("!!!VPZ FWPM J", 25))
# print(play_pass("BOY! YOU WANTED TO SEE HIM? IT'S YOUR FATHER:-)", 15))
# print(play_pass("FOR THIS REASON IT IS RECOMMENDED THAT PASSPHRASES NOT BE REUSED ACROSS DIFFERENT OR UNIQUE SITES AND SERVICES.", 15))
# print(play_pass("ONCE UPON A TIME YOU DRESSED SO FINE (1968)", 12))
# print(play_pass("AH, YOU'VE GONE TO THE FINEST SCHOOL ALL RIGHT, MISS LONELY", 12))
# print(play_pass("THE SPECIES, NAMED AFTER THE GREEK GOD OF THE UNDERWORLD, LIVES SOME 3,600 FEET UNDERGROUND.", 8))
