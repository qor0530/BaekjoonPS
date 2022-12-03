from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
que = [0]
for _ in range(n):
  num = int(input())
  if num == 0:
    que.pop()
  else:
    que.append(num)
    
sum = sum(que)
print(sum)