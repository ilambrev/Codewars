def solution(hour):
    hour_as_str = str(hour)

    if 3 <= len(hour_as_str) <= 4:
        return f"{hour_as_str[:len(hour_as_str)-2]}:{hour_as_str[len(hour_as_str)-2:]}"
    else:
        raise ValueError("Wrong hour value!")


# print(solution(800))
# print(solution(1000))
# print(solution(1451))
# print(solution(3351))
# print(solution(10000))
