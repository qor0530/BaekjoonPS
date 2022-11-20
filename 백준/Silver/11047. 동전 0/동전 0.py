from sys import stdin
input = stdin.readline
n, m = map(int,input().split())
value = []
count = 0
for _ in range(n):
  value.append(int(input()))
for i in range(1, n+1):
  coin = value[n-i]
  if m - coin >= 0:
    while m-coin >= 0:
      m -= coin
      count += 1
  else:
    pass
print(count)