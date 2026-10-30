def capitalize_words(message):
    return "".join(word[0].upper() + word[1:] for word in message.split())


def shortener(message):
    max_size = 160
    length = len(message)
    spaces = message.count(" ")

    if length > max_size and spaces > 0:
        diff = length - max_size

        if length - spaces > max_size:
            return capitalize_words(message)
        else:
            space_counter = 0

            for i in range(-1, -len(message), -1):
                if message[i] == " ":
                    space_counter += 1

                if space_counter == diff:
                    return message[:i] + capitalize_words(message[i:])

    else:
        return message


# tc1 = ('No one expects the Spanish Inquisition! Our chief weapon is surprise, '
#        'fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! '
#        'And that will be it.')
# tc1x = ('No one expects the Spanish Inquisition! Our chief weapon is surprise, '
#         'fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!'
#         'AndThatWillBeIt.')
# print(shortener(tc1))  # tc1x

# tc2 = "This message is already short enough!"
# print(shortener(tc2))  # tc2

# tc3 = ('ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
#        'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
#        'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon')
# print(shortener(tc3))  # tc3

# tc4 = ('SMS messages are limited to 160 characters. It tends to be irritating, '
#        'especially when freshly written message is 164 characters long. '
#        'SMS messages are limited to 160 characters. It tends to be irritating, '
#        'especially when freshly written message is 164 characters long.')
# tc4x = ('SMSMessagesAreLimitedTo160Characters.ItTendsToBeIrritating,Especially'
#         'WhenFreshlyWrittenMessageIs164CharactersLong.SMSMessagesAreLimitedTo160'
#         'Characters.ItTendsToBeIrritating,EspeciallyWhenFreshlyWrittenMessageIs'
#         '164CharactersLong.')
# print(shortener(tc4))  # tc4x
