import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]

def pibo(num):
  if num == 0:
    return [1,0]
  elif num == 1:
    return [0,1]
  else:
    if dp[num] == [0,0]:
      dp[num] = [pibo(num - 1)[0] + pibo(num - 2)[0], pibo(num - 1)[1] + pibo(num - 2)[1]]
    return dp[num]

for _ in range(n):
  num = int(input())
  a, b= pibo(num)
  print(a, b)
