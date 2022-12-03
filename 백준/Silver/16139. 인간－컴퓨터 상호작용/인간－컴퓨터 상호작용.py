import sys

input = sys.stdin.readline
string = list(input())
n = int(input())
for i in range(n):
  a, l, r = map(str, input().split())
  l = int(l)
  r = int(r)
  slice = [i for i in string[l:r + 1]]
  print(slice.count(a))
