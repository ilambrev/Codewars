def closest(strng):
    def calculate_number_weight(number):
        return sum([int(digit) for digit in number])

    numbers = strng.split()
    number_weights = [[calculate_number_weight(numbers[i]), i, int(numbers[i])] for i in range(len(numbers))]

    number_weights.sort(key=lambda number: number[0])

    result = []

    for i in range(len(number_weights) - 1):
        if i == 0:
            result.append(number_weights[0])
            result.append(number_weights[1])
            continue

        if abs(number_weights[i][0] - number_weights[i + 1][0]) < abs(result[0][0] - result[1][0]):
            result[0] = number_weights[i]
            result[1] = number_weights[i + 1]

    return result

# print(closest(""))
# print(closest("103 123 4444 99 2000 "))
# print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))
# print(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"))
# print(closest("241259 154 155206 194 180502 147 300751 200 406683 37 57"))
# print(closest("89998 187 126159 175 338292 89 39962 145 394230 167 1"))
# print(closest("403749 18 278325 97 304194 119 58359 165 144403 128 38"))
# print(closest("28706 196 419018 130 49183 124 421208 174 404307 60 24"))
# print(closest("189437 110 263080 175 55764 13 257647 53 486111 27 66"))
# print(closest("79257 160 44641 146 386224 147 313622 117 259947 155 58"))
# print(closest("315411 165 53195 87 318638 107 416122 121 375312 193 59"))