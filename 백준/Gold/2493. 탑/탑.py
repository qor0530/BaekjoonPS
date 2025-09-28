n = int(input())
tower = list(map(int, input().split()))
least = []
result = [0] * n
for i in range(n-1, -1, -1):
    num, pos = tower.pop(), i
    while least:
        if least[-1][0] < num:
            _ , s = least.pop()
            result[s] = pos+1
        else:
            break
    least.append((num, pos))
print(*result, sep=' ')