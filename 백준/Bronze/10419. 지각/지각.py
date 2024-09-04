n = int(input())

for _ in range(n):
    d = int(input())
    t = 0
    result = t**2 + t
    while result <= d:
        t += 1
        if t**2 + t > d:
            t -= 1
            break
        result = t**2 + t
    print(t)