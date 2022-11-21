from sys import stdin
input = stdin.readline
dp = [0 for _ in range(101)]
dp[1:10] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
def p(n):
  if n <= 10:
    return dp[n]
  else:
    if dp[n] == 0:
      dp[n] = p(n - 3) + p(n - 2)
    return dp[n]

n = int(input())
for _ in range(n):
  num = int(input())
  print(p(num))