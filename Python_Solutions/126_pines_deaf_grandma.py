def deaf_grandma(you):
    grandma_answers = []
    for my_words in you:
        if my_words == "BYE":
            grandma_answers.append("OK, BYE!")
            break
        elif my_words.upper() == my_words:
            grandma_answers.append("NO, NOT SINCE 1938!")
        else:
            grandma_answers.append("HUH?! SPEAK UP, SONNY!")

    return grandma_answers


# print(deaf_grandma(["hi grandma", "WHAT", "bye", "BYE"]))
# print(deaf_grandma(["BYE"]))
# print(deaf_grandma(["HELLO", "OK, BYE", "BYE"]))
# print(deaf_grandma(["good morning", "NICE TO SEE YOU", "BYE", "oh, I forgot", "nevermind", "see you"]))
# print(deaf_grandma(["Bye?", "BYE!", "BYE.", "BYE"]))
# print(deaf_grandma(["BYE8", "1 Ok, Bye!", "BYE"]))
