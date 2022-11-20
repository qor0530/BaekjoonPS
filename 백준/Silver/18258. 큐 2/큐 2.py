from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
que = deque()
for _ in range(n):
  order = input().rstrip()
  if order == 'pop':
    if que:
      print(que.popleft())
    else:
      print(-1)
  elif order == 'size':
    print(len(que))
  elif order == 'empty':
    if len(que) >= 1:
      print(0)
    else:
      print(1)
  elif order == 'front':
    if len(que) >= 1: 
      print(que[0])
    else: print(-1)
  elif order == 'back':
    if len(que) >= 1: 
      print(que[len(que) - 1])
    else: print(-1)
  else:
    num = int(order[5:])
    que.append(num)
  