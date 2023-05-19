def dp(que, target, tries):
    nq = []
    if not que:
        return -1
    for value in que:
        if value * 2 == target or value * 10 + 1 == target:
            return tries + 1
        else:
            if value * 2 < target:
                nq.append(value*2)
            if value * 10 + 1 < target:
                nq.append(value*10 + 1)
    return dp(nq, target, tries + 1)
    
a, b = map(int, input().split())
print(dp([a], b, 1))