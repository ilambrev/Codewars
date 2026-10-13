def count_longest_sub_string_of_contiguous_vowels(str):
    vowels = "aeiouAEIOU"
    i = 0
    count = 0

    while i < len(str):
        current_count = 0
        for s in str[i:]:
            i += 1
            if s in vowels:
                current_count += 1
            else:
                break

        count = max(count, current_count)

    return count


def sort_strings_by_vowels(seq):
    return sorted(seq, key=lambda s: count_longest_sub_string_of_contiguous_vowels(s), reverse=True)


# print(sort_strings_by_vowels(["aa","eee","oo","iiii"]))
# print(sort_strings_by_vowels(["a","e","ii","ooo","u"]))
# print(sort_strings_by_vowels(["ioue","ee","uoiea"]))
# print(sort_strings_by_vowels(["high","day","boot"]))
# print(sort_strings_by_vowels(["none","uuu","Yuuuge!!"]))
# print(sort_strings_by_vowels(["AIBRH","","YOUNG","GREEEN"]))
# print(sort_strings_by_vowels(["jyn","joan","jimmy","joey"]))
# print(sort_strings_by_vowels(["uijijeoj","lkjlkjww2","iiutrqy"]))
# print(sort_strings_by_vowels(["how about now","a beautiful trio of"]))
# print(sort_strings_by_vowels(["every","bataux","is","waaaay","loose"]))
