def solution(common):
    answer = 0
    ischa = True
    if common[-1] - common[-2] == common[-2] - common[-3]:
        ischa = True
    else:
        ischa = False
    if ischa:
        answer = common[-1] + common[-2] - common[-3]
    else:
        answer = common[-1] * (common[-2] / common[-3])
    return answer