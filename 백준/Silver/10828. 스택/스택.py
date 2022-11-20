from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
que = []
for _ in range(n):
  order = input().rstrip()
  if order == 'pop':
    if que:
      print(que.pop())
    else:
      print(-1)
  elif order == 'size':
    print(len(que))
  elif order == 'empty':
    if que:
      print(0)
    else:
      print(1)
  elif order == 'top':
    if que: 
      print(que[-1])
    else:
      print(-1)
  else:
    num = int(order[5:])
    que.append(num)
  