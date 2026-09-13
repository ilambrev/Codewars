def wave(people):
    wave_elements = []

    for i in range(len(people)):
        symbol = people[i]

        if symbol.isalpha():
            element = symbol.upper() + people[i+1:] if i == 0 else people[:i] + symbol.upper() + people[i+1:]
            wave_elements.append(element)

    return wave_elements

# print(wave("hello"))
# print(wave("codewars"))
# print(wave(""))
# print(wave("two words"))
# print(wave(" gap "))
# print(wave("a       b    "))
# print(wave("this is a few words"))
