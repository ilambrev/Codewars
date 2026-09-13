def order_weight(strng):
    weights = [[w, sum([int(d) for d in w])] for w in strng.split()]

    return " ".join([w[0] for w in sorted(weights, key=lambda x: (x[1], x[0]))])

# print(order_weight("103 123 4444 99 2000"))
# print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
# print(order_weight(""))
