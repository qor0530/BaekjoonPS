N = int(input())
parts = []
for i in range(N):
    part = list(map(int, input().split()))
    count = part[0]
    time = part[1:]
    parts.append(sum(time))

parts.sort()

total = 0
for i in range(N):
    total += parts[i] * (N - i)
    
print(total)