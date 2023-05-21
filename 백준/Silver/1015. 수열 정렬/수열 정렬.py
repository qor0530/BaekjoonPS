N = int(input())
A = list(map(int, input().split()))
P = [0 for _ in range(N)]
count = 0
for i in range(1, 1001): 
    for j in range(N): 
        if A[j] == i:
            P[j] += count
            count += 1
        
print(*P)
