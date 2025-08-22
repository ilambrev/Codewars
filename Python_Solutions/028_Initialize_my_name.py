def initialize_names(name):
    name_parts = name.split()

    if len(name_parts) > 2:
        for i in range(1, len(name_parts) - 1):
            name_parts[i] = name_parts[i][0:1] + '.'

    return ' '.join(name_parts)

# print(initialize_names('Jack Ryan'))
# print(initialize_names('Lois Mary Lane'))
# print(initialize_names('Dimitri'))
# print(initialize_names('Alice Betty Catherine Davis'))