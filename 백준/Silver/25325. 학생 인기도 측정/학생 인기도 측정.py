from heapq import heappop, heappush
n = int(input())

std = dict()
std_l = input().split()

for i in range(n):
    std[std_l[i]] = 0

for i in range(n):
    likes = input().split()
    for j in range(len(likes)):
        std[likes[j]] += 1
fame = []
for key, item in std.items():
    heappush(fame, (-item, key))

for i in range(n):
    item , key = heappop(fame)
    print(key, -item)