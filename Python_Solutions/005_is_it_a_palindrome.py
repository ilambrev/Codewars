def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# print(is_palindrome("a"))
# print(is_palindrome("aba"))
# print(is_palindrome("Abba"))
# print(is_palindrome("malam"))
# print(is_palindrome("walter"))
# print(is_palindrome("kodok"))
# print(is_palindrome("Kasue"))