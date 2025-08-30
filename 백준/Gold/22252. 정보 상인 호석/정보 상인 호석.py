from collections import defaultdict
from heapq import heappop, heappush
q = int(input())


golila = defaultdict(list)
cost = 0
for _ in range(q):
    data = list(input().split())
    cmd = data[0]
    name = data[1]
    if cmd == '1': #get
        k = data[2]
        c = list(map(int, data[3:]))
        for i in range(len(c)):
            heappush(golila[name], -c[i])
    else: #buy
        b = int(data[2])
        for i in range(b):
            if golila[name]:
                c = heappop(golila[name])
                cost += -c
            else:
                break

print(cost)