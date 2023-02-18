import sys
input = sys.stdin.readline
from itertools import combinations

nlist = list(input().split())
while(nlist[0] != '0'):
    combilist = combinations(nlist[1:], 6)
    for combi in combilist:
        print(' '.join(combi))
    print()
    nlist = list(input().split())