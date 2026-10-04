def pascal(p):
    triangle = []

    for i in range(1, p + 1):
        row = []

        if i == 1:
            row.append(1)
        else:
            for j in range(1, i + 1):
                if j == 1 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-2][j-2] + triangle[i-2][j-1])

        triangle.append(row)

    return triangle


# print(pascal(1))
# print(pascal(5))
