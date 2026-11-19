def race(v1, v2, g):
    if v1 < v2:
        t_sec = int(g / ((v2 - v1) / 3600))
        hours = int(t_sec / 3600)
        minutes = int((t_sec - hours * 3600) / 60)
        seconds = t_sec - (hours * 3600 + minutes * 60)

        return [hours, minutes, seconds]

    return None


# print(race(720, 850, 70))
# print(race(80, 91, 37))
# print(race(820, 81, 550))
