def off(n):
    switches = []

    for step in range(1, n + 1):
        for i in range(step - 1, n, step):
            if step == 1:
                switches.append(0)
            else:
                switches[i] = abs(switches[i] - 1)

    return [i + 1 for i in range(0, n) if switches[i] == 0]

# print(off(1))
# print(off(2))
# print(off(4))
# print(off(9))
# print(off(12))