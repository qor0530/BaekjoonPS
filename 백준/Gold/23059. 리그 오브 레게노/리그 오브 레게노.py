import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
items = dict()
inbound = dict()
result = []
all = set()
for _ in range(n):
    first_item, next_item = input().split()
    if first_item not in inbound.keys():
        inbound[first_item] = 0
    try:    
        inbound[next_item] += 1
    except:
        inbound[next_item] = 1    
    try:
        items[first_item].append(next_item)
    except:
        items[first_item] = [next_item]
    if first_item not in all:
        all.add(first_item)
    if next_item not in all:
        all.add(next_item)

Q = deque([])
for item in inbound.keys():
    if inbound[item] == 0:
        Q.append(item)

real_result = []
count = len(Q)
while Q:
    if count == 0:
        real_result += sorted(result)
        result = []
        count = len(Q) - 1
    else:
        count -= 1
    popitem = Q.popleft()
    result.append(popitem)
    if popitem not in items.keys():
        continue
    for item in items[popitem]:
        inbound[item] -= 1
        if inbound[item] == 0:
            Q.append(item)
if count == 0:
    real_result += sorted(result)
if len(all) == len(real_result):
    for item in real_result:
        print(item)
else:
    print(-1)