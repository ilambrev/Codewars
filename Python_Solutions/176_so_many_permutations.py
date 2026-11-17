import itertools


def permutations(s):
    return set("".join(combo) for combo in itertools.permutations([e for e in s], len(s)))


# print(sorted(permutations("a")))
# print(sorted(permutations("ab")))
# print(sorted(permutations("aabb")))
