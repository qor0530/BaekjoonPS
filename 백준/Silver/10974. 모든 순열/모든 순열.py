import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input().rstrip())

nlist = [k for k in range(1, n+1)]
comlist = list(permutations(nlist, n))
for i in range(len(comlist)):
    print(*comlist[i])