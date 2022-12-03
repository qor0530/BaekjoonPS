import sys

input = sys.stdin.readline

n = int(input())
num = n + 1
dp = [0 for _ in range(num + 1)]
dp[0] = 0
dp[1] = 1
for i in range(2, num + 1):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[num]%10007)
