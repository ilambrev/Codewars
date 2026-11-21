def triple_double(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    for i in range(10):
        if str(i) * 3 in num1_str and str(i) * 2 in num2_str:
            return 1

    return 0


# print(triple_double(123123123, 123123))
# print(triple_double(111, 88))
# print(triple_double(111000, 100))
# print(triple_double(111888, 1188))
# print(triple_double(451999277, 41177722899))
# print(triple_double(1222345, 12345))
# print(triple_double(12345, 12345))
# print(triple_double(666789, 12345667))
# print(triple_double(10560002, 100))
# print(triple_double(1112, 122))
