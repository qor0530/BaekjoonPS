import sys

input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
sorted_list = list(set(nlist[:]))
sorted_list.sort()
dic = {int: i for i, int in enumerate(sorted_list)}
for i in range(n):
  print(dic[nlist[i]], end=' ')