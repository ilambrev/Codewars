def remove_exclamation_marks(s):
    clear_string = ""
    for letter in s:
        if letter != "!":
            clear_string += letter
    return clear_string

# print(remove_exclamation_marks("Hello World!"))
# print(remove_exclamation_marks("Hello World!!!"))
# print(remove_exclamation_marks("Hi! Hello!"))
# print(remove_exclamation_marks(""))
# print(remove_exclamation_marks("Oh, no!!!"))