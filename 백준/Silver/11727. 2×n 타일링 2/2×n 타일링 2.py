n = int(input())
dp = [0]*(n+2)
k = 2
dp[1] = 1
dp[2] = 3
if n > 2:
    while k != n:
        k+=1
        dp[k] = dp[k-1] + dp[k-2]*2

print((dp[n]%10007))