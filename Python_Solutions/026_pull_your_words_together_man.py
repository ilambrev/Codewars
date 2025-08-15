def sentencify(words):
    if words:
        words[0] = words[0][0].upper() + words[0][1:]
        return ' '.join(words) + '.'
    else:
        return ''

# print(sentencify(["i", "am", "an", "AI"]))
# print(sentencify(["yes"]))
# print(sentencify(["FIELDS", "of", "CORN", "are", "to", "be", "sown"]))
# print(sentencify(["i'm", "afraid", "I", "can't", "let", "you", "do", "that"]))