import sys
input = sys.stdin.readline
from collections import deque

string = deque(list(input().rstrip()))
boom = list(input().rstrip())
stringlen = len(string)
boomlen = len(boom)
boomlist = []
for i in range(stringlen):
    boomlist.append(string.popleft())
    if boomlist[-1] == boom[-1]:
        if boomlist[len(boomlist)-boomlen:len(boomlist)] == boom:
            for i in range(boomlen):
                boomlist.pop()

if boomlist:
    print(''.join(boomlist))
else:
    print('FRULA')