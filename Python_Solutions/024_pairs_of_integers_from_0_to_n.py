def generate_pairs(n):
    result = []
    for i in range(0, n + 1):
        for j in range(i, n + 1):
                result.append([i, j])

    return result

# print(generate_pairs(2))
# print(generate_pairs(0))