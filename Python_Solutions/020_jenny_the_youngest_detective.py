def missing(nums, s):
    string_without_spaces = s.replace(' ', '').lower()
    word = []

    list.sort(nums)

    for num in nums:
        if num >= len(string_without_spaces):
            return 'No mission today'
        else:
            word.append(string_without_spaces[num])

    return ''.join(word)

# print(missing([0, 3, 5], 'I love you'))
# print(missing([29, 31, 8], 'The quick brown fox jumps over the lazy dog'))
# print(missing([12, 4, 6], 'Good Morning'))