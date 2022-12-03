from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
answer = defaultdict(int)
for i in range(len(mlist)):
    answer[mlist[i]]
for i in range(len(nlist)):
    if answer[nlist[i]] == 0:
        answer[nlist[i]] = 1
for i in range(len(mlist)):
    print(answer[mlist[i]])