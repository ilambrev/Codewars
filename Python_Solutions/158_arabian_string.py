def camelize(str):
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    words = "".join([char if char in allowed_characters else " " for char in str.lower()]).split()

    return "".join(word.capitalize() for word in words)


# print(camelize("java script"))
# print(camelize("cODE warS"))
