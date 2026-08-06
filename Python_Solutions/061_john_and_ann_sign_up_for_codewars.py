def john(n):
    ann_katas = []
    john_katas = []
    for i in range(n):
        if i == 0:
            ann_katas.append(1)
            john_katas.append(0)
        else:
            t = ann_katas[john_katas[i - 1]]
            john_katas.append(i - t)
            t = john_katas[ann_katas[i - 1]]
            ann_katas.append(i - t)
    return john_katas


def ann(n):
    ann_katas = []
    john_katas = []
    for i in range(n):
        if i == 0:
            ann_katas.append(1)
            john_katas.append(0)
        else:
            t = ann_katas[john_katas[i - 1]]
            john_katas.append(i - t)
            t = john_katas[ann_katas[i - 1]]
            ann_katas.append(i - t)
    return ann_katas


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))


# print(john(11))
# print(ann(6))
# print(sum_john(75))
# print(sum_ann(115))
