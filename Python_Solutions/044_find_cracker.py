def find_hack(arr):
    points = {'A': 30, 'B': 20, 'C': 10, 'D': 5}
    hacked_entries = []

    for entry in arr:
        name = entry[0]
        scores = entry[1]
        grades = entry[2]

        if scores > 200:
            hacked_entries.append(name)
            continue

        real_scores = sum([points[grade] for grade in grades if grade in points])

        if len([grade for grade in grades if not grade == 'B' and not grade == 'A']) == 0 and len(grades) >= 5:
            real_scores += 20

        if real_scores > 200:
            real_scores = 200

        if not real_scores == scores:
            hacked_entries.append(name)

    return hacked_entries

# print(find_hack([
#     ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
#     ["name2", 120, ["B", "A", "A", "A"]],
#     ["name3", 160, ["B", "A", "A", "A", "A"]],
#     ["name4", 140, ["B", "A", "A", "C", "A"]]
# ]))