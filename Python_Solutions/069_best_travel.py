def count_sum(binary_num, ls):
    current_sum = 0
    for i in range(len(binary_num)):
        if binary_num[i] == "1":
            current_sum += ls[i]

    return current_sum


def choose_best_sum(t, k, ls):
    best_sum = None

    for i in range(2 ** len(ls)):
        binary_num = bin(i)[2:].zfill(len(ls))
        if binary_num.count("1") == k:
            current_sum = count_sum(binary_num, ls)
            if current_sum <= t and (best_sum == None or best_sum < current_sum):
                best_sum = current_sum

    return best_sum

# ts = [50, 55, 56, 57, 58]
# print(choose_best_sum(163, 3, ts))  # 163
        
# ts = [50]
# print(choose_best_sum(163, 3, ts))  # None
        
# ts = [91, 74, 73, 85, 73, 81, 87]
# print(choose_best_sum(230, 3, ts))  # 228
# print(choose_best_sum(331, 2, ts))  # 178
# print(choose_best_sum(331, 4, ts))  # 331
# print(choose_best_sum(331, 5, ts))  # None
# print(choose_best_sum(331, 1, ts))  # 91
# print(choose_best_sum(700, 6, ts))  # 491

# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 4, xs))  # 230
# print(choose_best_sum(430, 5, xs))  # 430
# print(choose_best_sum(430, 8, xs))  # None
# print(choose_best_sum(880, 8, xs))  # 876
# print(choose_best_sum(2430, 15, xs))  # 1287
# print(choose_best_sum(100, 2, xs))  # 100
# print(choose_best_sum(276, 3, xs))  # 276
# print(choose_best_sum(3760, 17, xs))  # 3654
# print(choose_best_sum(3760, 40, xs))  # None
# print(choose_best_sum(50, 1, xs))  # 50
# print(choose_best_sum(1000, 18, xs))  # None

# xs = [100, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 4, xs))  # None
# print(choose_best_sum(230, 2, xs))  # 223
# print(choose_best_sum(2333, 1, xs))  # 2333
# print(choose_best_sum(2333, 8, xs))  # 825

# xs = [1000, 640, 1230, 2333, 1440, 500, 1320, 1230, 340, 890, 732, 1346]
# print(choose_best_sum(2300, 4, xs))  # 2212
# print(choose_best_sum(2300, 5, xs))  # None
# print(choose_best_sum(2332, 3, xs))  # 2326
# print(choose_best_sum(23331, 8, xs))  # 10789
# print(choose_best_sum(331, 2, xs))  # None