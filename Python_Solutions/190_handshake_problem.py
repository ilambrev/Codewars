from math import sqrt, ceil


def get_participants(handshakes):
    if handshakes == 0:
        return 0

    d = (-1) ** 2 - 4 * (-2 * handshakes)
    n1 = (1 + sqrt(d)) / 2
    n2 = (1 - sqrt(d)) / 2

    return ceil(max(n1, n2))


# print(get_participants(0))
# print(get_participants(1))
# print(get_participants(3))
# print(get_participants(6))
# print(get_participants(7))
