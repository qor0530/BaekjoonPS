n, k = map(int, input().split())

l = []
t = []

for _ in range(k):
    a, b = map(int, input().split())
    l.append(a)
    t.append(b)

dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if t[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t[i-1]]+l[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[k][n])