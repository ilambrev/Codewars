def hello(name=None):
    if (name):
        return f"Hello, {name.capitalize()}!"
    else:
        return "Hello, World!"

# print(hello("John"))
# print(hello("aLIce"))
# print(hello(""))
# print(hello())