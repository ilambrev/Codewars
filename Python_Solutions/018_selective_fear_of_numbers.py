def am_i_afraid(day, num):
    match day:
        case 'Monday':
            return num == 12
        case 'Tuesday':
            return num > 95
        case 'Wednesday':
            return num == 34
        case 'Thursday':
            return num == 0
        case 'Friday':
            return num % 2 == 0
        case 'Saturday':
            return num == 56
        case 'Sunday':
            return num == 666 or num == -666
        case _:
            return False

# print(am_i_afraid('Monday', 13))
# print(am_i_afraid('Sunday', -666))
# print(am_i_afraid('Tuesday', 2))
# print(am_i_afraid('Tuesday', 965))
# print(am_i_afraid('Friday', 2))