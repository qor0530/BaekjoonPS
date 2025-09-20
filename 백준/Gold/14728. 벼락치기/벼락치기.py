n, t = map(int, input().split())
k = []
s = []
for i in range(n):
    a, b = map(int, input().split())
    k.append(a)
    s.append(b)

dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if k[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k[i-1]] + s[i-1])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[n][t])