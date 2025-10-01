from heapq import heappop, heappush

N = int(input())
meeting = []

for i in range(N):
    start, end = map(int, input().split())
    heappush(meeting, (end, start))

now = 0
count = 0
while meeting:
    end, start = heappop(meeting)
    if now <= start:
        now = end
        count += 1
print(count)