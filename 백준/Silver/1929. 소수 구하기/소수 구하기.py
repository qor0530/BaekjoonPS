import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = [True] * (m + 1)
a[0] = a[1] = False

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, m + 1, i):
            a[j] = False

for i in range(n,m+1):
    if a[i]:
        print(i)