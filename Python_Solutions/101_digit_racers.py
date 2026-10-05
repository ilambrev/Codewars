def calculate_digits_scores(s):
    digits_scores = {}

    for i in range(len(s)):
        digit = s[i]

        if not digit in digits_scores:
            digits_scores[digit] = [0, 0]

        digits_scores[digit][0] += 1
        digits_scores[digit][1] = i

    return digits_scores


def calculate_result(digit_scores, places):
    result = []

    digit_scores_sorted = [[k, v[0]] for k, v in sorted(digit_scores.items(), key=lambda item: (item[1][0], item[1][1]), reverse=True)]

    current_repeats = digit_scores_sorted[0][1]
    current_places_index = 0
    grouped_digits = []

    for digit, repeats in digit_scores_sorted:
        if repeats == current_repeats:
            grouped_digits.append(digit)
        else:
            current_place = places[current_places_index]
            result.append(f"{current_place}{', '.join(grouped_digits)}")
            grouped_digits.clear()
            current_places_index += 1
            current_repeats = repeats
            grouped_digits.append(digit)

    result.append(f"{places[current_places_index]}{', '.join(grouped_digits)}")

    return result


def find_absent_digits(present_digits):
    return [str(i) for i in range(10) if not str(i) in present_digits]


def digit_racers(s):
    places = [
        "1st place: ",
        "2nd place: ",
        "3rd place: ",
        "4th place: ",
        "5th place: ",
        "6th place: ",
        "7th place: ",
        "8th place: ",
        "9th place: ",
        "10th place: "
    ]

    digits_scores = calculate_digits_scores(s)

    result = calculate_result(digits_scores, places)

    absent_digits = find_absent_digits(digits_scores.keys())

    if absent_digits:
        result.append(f"Absent digits: {', '.join(absent_digits)}")
    else:
        result.append("All digits present")

    return "\n".join(result)


# print(digit_racers("7171"))
# print(digit_racers("5501234567789"))
# print(digit_racers("226260"))
# print(digit_racers("666661117777009"))
# print(digit_racers("01234567899876543210"))
# print(digit_racers("555055007030059926922294411"))
# print(digit_racers("5355555555022222222999999111211199333337177770004448865"))
