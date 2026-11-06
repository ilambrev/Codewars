def remove_duplicate(a):
    return [eval(s) for s in sorted(set(str(d) for d in a))]


# Nodes = [
#     {'data': {'id': 'A'}},
#     {'data': {'id': 'A'}},
#     {'data': {'id': 'A'}},
#     {'data': {'id': 'A'}},
#     {'data': {'id': 'B'}},
#     {'data': {'id': 'B'}},
#     {'data': {'id': 'D'}},
#     {'data': {'id': 'D'}},
#     {'data': {'id': 'B'}},
#     {'data': {'id': 'B'}},
#     {'data': {'id': 'B'}},
#     {'data': {'id': 'B'}},
#     {'data': {'id': 'E'}},
#     {'data': {'id': 'E'}}]

# print(remove_duplicate(Nodes))
