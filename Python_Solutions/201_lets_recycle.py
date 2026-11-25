def recycle(a):
    beans = ([], [], [], [])
    routes = {"paper": 0, "glass": 1, "organic": 2, "plastic": 3}

    for o in a:
        beans[routes[o["material"]]].append(o["type"])

        if "secondMaterial" in o:
            beans[routes[o["secondMaterial"]]].append(o["type"])

    return beans


# a = [
#     {"type": "rotten apples", "material": "organic"},
#     {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
#     {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
#     {"type": "amazon box", "material": "paper"},
#     {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
# ]
# print(recycle(a))
