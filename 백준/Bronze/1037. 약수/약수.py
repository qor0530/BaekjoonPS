nc = int(input())
n = list(map(int, input().split()))
N = 0

for i in range(max(n), 1000001):
    for j in range(nc):
        if i % n[j] == 0 and i // n[j] != 1 and i // n[j] in n: 
            pass
        else:
            break
        if j == nc-1:
            N = i
    if N != 0:
        break
print(N)
