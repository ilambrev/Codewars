def monkey_talk(phrase):
    return f"{' '.join('eek' if word[0].lower() in 'aeiou' else 'ook' for word in phrase.split()).capitalize()}."


# print(monkey_talk("Hello"))
# print(monkey_talk("Everyone"))
# print(monkey_talk("Hello Everyone"))
# print(monkey_talk("Everyone Hello"))
