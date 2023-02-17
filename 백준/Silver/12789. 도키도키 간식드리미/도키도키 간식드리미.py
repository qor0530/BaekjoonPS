import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
nlist = list(map(int, input().split()))
numlist = nlist
Nice = 0
passNum = 1
standing = []
for i in nlist:
    if i != passNum:
        while standing and standing[-1] == passNum:
            standing.pop()
            passNum += 1
        standing.append(i)
    else:
        passNum += 1
for i in standing[::-1]:
    if i != passNum:
        Nice += 1
        break
    else:
        passNum += 1
if Nice != 1:
    print('Nice')
else:
    print('Sad')