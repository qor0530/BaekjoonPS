import sys
input = sys.stdin.readline

num = 0 
n = int(input())
dp = [0 for _ in range(n + 1)]
for i in range(n + 1):
  if i == 0:
    dp[i] = 1
  elif i == 1:
    dp[i] = 1
  else:
    dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[n])