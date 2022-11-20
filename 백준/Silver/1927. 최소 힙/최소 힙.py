from queue import PriorityQueue
import sys

q = PriorityQueue()
n = int(input())
for _ in range(n):
  x = int(sys.stdin.readline())
  if x == 0:
    if q.qsize() == 0:
      print(0)
    else:
      print(q.get(x))
  else:
    q.put(x)