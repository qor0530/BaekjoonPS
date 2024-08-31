n = int(input())
a = list(map(int, input().split()))
missing = []
for i in range(1, n+1):
    if i not in a:
        missing.append(i)
print(*missing, sep=' ')
