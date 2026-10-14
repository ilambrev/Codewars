def grabscrab(said, possible_words):
    said_sorted = sorted(said)

    return [w for w in possible_words if sorted(w) == said_sorted]


# print(grabscrab("trisf", ["first"]))
# print(grabscrab("oob", ["bob", "baobab"]))
# print(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]))
# print(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]))
# print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))
# print(grabscrab("ourf", ["one", "two", "three"]))
# print(grabscrab("racer", ["crazer", "carer", "racar", "caers", "racer"]))
# print(grabscrab("abba", ["aabb", "abcd", "bbaa", "abbb", "aaab"]))
# print(grabscrab("otni", ["child", "first", "not", "into", "toni", "thing"]))
