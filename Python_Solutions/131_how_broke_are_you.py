def broke_count(expenditures):
    events = 0
    length = len(expenditures)
    i = 0

    while i < length:
        if length - i >= 7 and sum(1 for e in expenditures[i:i+7] if e <= 10) == 7:
            events += 1
            i += 7
        elif length - i >= 3 and sum(1 for e in expenditures[i:i+3] if e <= 7) == 3:
            events += 1
            i += 3
        elif expenditures[i] <= 3:
            events += 1
            i += 1
        else:
            i += 1

    return events


# print(broke_count([2]))
# print(broke_count([5]))
# print(broke_count([5, 6, 7]))
# print(broke_count([5, 6, 8]))
# print(broke_count([9, 8, 10, 9, 7, 6, 5]))
# print(broke_count([9, 8, 10, 12, 7, 6, 5]))
# print(broke_count([2, 5, 6, 9, 8, 7, 6]))
# print(broke_count([2, 20, 2]))
# print(broke_count([5, 6, 7, 20, 5, 6, 7]))
# print(broke_count([]))
