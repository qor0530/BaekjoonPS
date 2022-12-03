import sys

input = sys.stdin.readline
n, m = map(int, input().split())
numlist = list(map(int, input().split()))
presum = [0]
for i in range(1, n + 1):
  presum.append(presum[i - 1] + numlist[i - 1])
for _ in range(m):
  sum = 0
  start, end = map(int, input().split())
  print(presum[end] - presum[start - 1])
