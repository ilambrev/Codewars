def sc(arr):
    nums = {}

    for a in arr:
        for e in a:
            nums[e] = nums.get(e, 0) + 1

    max_repeats = max(nums.values()) if nums else 0
    nums_to_compare = [k for k, v in nums.items() if v == max_repeats]

    result = []

    for a in arr:
        sub_arr = []
        for e in a:
            if not e in nums_to_compare:
                sub_arr.append(e)
        result.append(sub_arr)

    return result

# print(sc([[3,3,3,3,3,3,3,3,3]]))
# print(sc([[3,3,3,3,3,3,3,3,3,4,5]]))
# print(sc([[3,4,5]]))
# print(sc([[3,4,5],[3,4,5]]))
# print(sc([[3,4,5],[4,4,4]]))
# print(sc([[3,4,4,5],[3,4,4,5],[3,4,4,5],[3,4,4,5]]))
# print(sc([[]]))
# print(sc([]))
