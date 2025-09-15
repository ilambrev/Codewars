words = ['FEED', 'BAIL', 'DATA', 'GAME', 'BALL', 'BEAT', 'NEED', 'DATE', 'GATE', 'KEEL', 'BILL', 'BITE', 'HERE', 'WAGE',
         'FIRE', 'PAIL', 'KILL', 'WEEK', 'BYTE', 'LOOK', 'WIRE', 'VIEW', 'YOLK', 'ALIBI', 'CAGES', 'DECAY', 'BRAIN',
         'LABOR', 'TRADE', 'CAUSE', 'DATES', 'CAVES', 'GATES', 'RAISE', 'STAGE', 'USAGE', 'SALES', 'SEALS', 'SLEDS',
         'LORAN', 'SAILS', 'DOSES', 'TODAY', 'BUSES', 'WATER', 'SOLES', 'GUEST', 'ISSUE', 'WIRES', 'TOWER', 'BUOYS',
         'IVORY', 'OCEANS', 'SECOND', 'CODERS', 'FORCES', 'REASON', 'GASOLINE']

def longest_word(letters):
    if not letters:
        return None

    def generate_letter_dictionary(string):
        dictionary = {}

        for letter in string:
            if not letter in dictionary:
                dictionary[letter] = 0

            dictionary[letter] += 1

        return dictionary

    letters_dict = generate_letter_dictionary(letters)

    longest_words = []

    for word in words:
        word_dict = generate_letter_dictionary(word)

        for key in word_dict:
            if key not in letters_dict or word_dict[key] > letters_dict[key]:
                break

        else:
            if not longest_words or len(word) == len(longest_words[0]):
                longest_words.append(word)
            elif len(word) > len(longest_words[0]):
                longest_words.clear()
                longest_words.append(word)

    longest_words.sort()

    return None if not longest_words else longest_words

# print(longest_word('GQEMAUVXY'))
# print(longest_word('TDWAYZROE'))
# print(longest_word('EAEEAYITB'))
# print(longest_word('AKUIYOOLO'))
# print(longest_word('GVDTCAESU'))
# print(longest_word(""))
# print(longest_word("MKMKMKMKM"))
# print(longest_word("IIIWUGEZI"))
# print(longest_word("WTGAEUAUD"))
# print(longest_word("MVIIIZEKQ"))
# print(longest_word("SIARIERRW"))
# print(longest_word("YIOVOORUF"))
# print(longest_word("EWFEREIUH"))
# print(longest_word("NLGIEOTSA"))
# print(longest_word("ASIULSIEI"))
# print(longest_word("AFDEEONEA"))
# print(longest_word("OFRDACESN"))
# print(longest_word("YBOEDSLSU"))
# print(longest_word("GIABBLPBL"))
# print(longest_word("RAOQILBIN"))
# print(longest_word("KIEWVELIL"))
# print(longest_word("DDAYCEEQR"))