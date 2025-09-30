n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = list(0 for _ in range(1+k))
dp[0] = 1
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] += dp[j - coin[i]]

print(dp[-1])