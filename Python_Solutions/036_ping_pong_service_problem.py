def service(score):
    (first_score, second_score) = score.split(':')
    score_sum = int(first_score) + int(second_score)

    if score_sum <= 40:
        cycles = score_sum // 5
    else:
        cycles = (score_sum - 40) // 2
    return 'first' if cycles % 2 == 0 else 'second'

# print(service('0:0'))
# print(service('3:2'))
# print(service('21:20'))
# print(service('21:22'))