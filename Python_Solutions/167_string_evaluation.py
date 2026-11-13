def string_evaluation(strng, conditions):
    result = []
    for condition in conditions:
        first_char_count = int(condition[0]) if condition[0].isnumeric() else strng.count(condition[0])
        second_char_count = int(condition[-1]) if condition[-1].isnumeric() else strng.count(condition[-1])
        result.append(eval(f"{first_char_count}{condition[1:-1]}{second_char_count}"))

    return result


# print(string_evaluation("aab#HcCcc##l#", ['a<b', '#==4', 'c>=C', 'H!=a']))
# print(string_evaluation("abc#$%KDAyyaa@@@", ['#>@', 'A==2', 'a>A', '$!=2']))
# print(string_evaluation("abb", ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1']))
