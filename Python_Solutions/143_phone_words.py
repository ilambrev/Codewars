def group_nums(string_of_nums, nums_to_letters):
    result = []
    current_num = ""

    for num in string_of_nums:
        if current_num:
            last_num = current_num[-1]

            if (last_num == num and len(current_num) == len(nums_to_letters[num])) or last_num != num:
                result.append(current_num)
                current_num = ""

        current_num += num

    if current_num:
        result.append(current_num)

    return result


def phone_words(string_of_nums):
    nums_to_letters = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": " "
    }

    groups = group_nums(string_of_nums, nums_to_letters)

    return "".join("" if group[0] == "1" else nums_to_letters[group[0]][len(group) - 1] for group in groups)


# print(phone_words("443355555566604466690277733099966688"))
# print(phone_words("55282"))
# print(phone_words("44460208337777833777"))
# print(phone_words("22266631339277717777"))
# print(phone_words("66885551555"))
# print(phone_words("833998"))
# print(phone_words("000"))
# print(phone_words("7999844666166"))
# print(phone_words("55886444833"))
# print(phone_words("271755533"))
# print(phone_words(""))
# print(phone_words("111"))
