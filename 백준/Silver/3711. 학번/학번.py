n = int(input())
for _ in range(n):
    m = int(input())
    std_id = [int(input()) for _ in range(m)]
    for i in range(1, 10**6):
        remain = []
        for j in range(m):
            if std_id[j] % i not in remain:
                remain.append(std_id[j] % i)
            else:
                break
        if len(remain) == m:
            print(i)
            break