def longest_palindrome(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) + 1 - i):
            sub_str = s[j:j+i]
            if sub_str == sub_str[::-1]:
                return len(sub_str)

    return 0


# print(longest_palindrome("a"))
# print(longest_palindrome("aa"))
# print(longest_palindrome("baa"))
# print(longest_palindrome("aab"))
# print(longest_palindrome("abcdefghba"))
# print(longest_palindrome("baablkj12345432133d"))
