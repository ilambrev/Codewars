# arr1 = ['super', 'bow', 'bowl', 'tar', 'get', 'book', 'let']
# arr2 = ['bow', 'crystal', 'organic', 'ally', 'rain', 'line']
# arr3 = ['top', 'main', 'tree', 'ally', 'fin', 'line']
# arr4 = ['bel', 'bed', 'low', 'grab', 'be', 'knight']

def compound_match(words, target):
    for i in range(1, len(target)):
        if target[:i] in words:
            index1 = words.index(target[:i])

            if target[i:] in words:
                index2 = words.index(target[i:])
                indexes_sorted = sorted([index1, index2])

                return [words[indexes_sorted[0]], words[indexes_sorted[1]], [index1, index2]]

    return None

# print(compound_match(arr1, 'superbowl'))
# print(compound_match(arr2, 'crystalline'))
# print(compound_match(arr2, 'rainbow'))
# print(compound_match(arr2, 'organically'))
# print(compound_match(arr3, 'mainline'))
# print(compound_match(arr3, 'treetop'))
# print(compound_match(arr3, 'finally'))
# print(compound_match(arr3, 'treefinally'))
# print(compound_match(arr4, 'below'))
# print(compound_match(arr4, 'bellow'))
# print(compound_match(arr4, 'beknight'))