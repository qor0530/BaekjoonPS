N, K = map(int, input().split())

live = [i for i in range(1, N+1)]
dead = []

count = -1
for i in range(N):
    for j in range(K):
        count += 1
        count %= len(live)
    dead.append(live.pop(count))
    count -= 1
    if count >= 0:
        count %= len(live)
    
print("<", end="")
print(*dead,sep=", ", end="")
print(">", end="")