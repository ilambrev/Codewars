def isomorph(a, b):
    if len(a) != len(b):
        return False

    letters_mapping_a = {}
    letters_mapping_b = {}

    for i in range(0, len(a)):
        if not a[i] in letters_mapping_a and not b[i] in letters_mapping_b:
            letters_mapping_a[a[i]] = b[i]
            letters_mapping_b[b[i]] = a[i]
        elif a[i] in letters_mapping_a:
            if b[i] != letters_mapping_a[a[i]]:
                return False
        else:
            return False

    return True

# print(isomorph("ESTATE", "DUELED"))
# print(isomorph("XXX", "YYY"))
# print(isomorph("SEE", "SAW"))
# print(isomorph("XXY", "XYY"))
# print(isomorph("CBAABC", "DEFFED"))
# print(isomorph("RAMBUNCTIOUSLY", "THERMODYNAMICS"))
# print(isomorph("AB", "CC"))
# print(isomorph("ABAB", "CD"))