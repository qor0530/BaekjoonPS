from heapq import heappop, heappush
import sys
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):
  num = int(input())
  if num == 0:
    if heap:
      print(heappop(heap)[1])
    else:
      print(0)
  else:
    heappush(heap, (-num, num))