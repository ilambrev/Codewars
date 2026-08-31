def max_ball(v0):
    g = 9.81
    v = (v0 * 1000) / 3600
    h = 0.0
    t = 0

    ball_heights = {}

    while h >= 0:
        ball_heights[t] = h
        t += 1
        t0 = t / 10
        h = v * t0 - 0.5 * g * t0 * t0

    return max(ball_heights, key=ball_heights.get)


# print(max_ball(37))
# print(max_ball(45))
# print(max_ball(99))
# print(max_ball(85))
