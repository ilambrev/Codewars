def remove(st):
    words = st.split()

    for i in range(0, len(words)):
        while words[i][-1] is '!':
            words[i] = words[i][:-1]

    return ' '.join(words)

# print(remove('Hi!'))
# print(remove('Hi!!!'))
# print(remove('!Hi'))
# print(remove('!Hi!'))
# print(remove('Hi! Hi!'))
# print(remove('!!!Hi !!hi!!! !hi'))