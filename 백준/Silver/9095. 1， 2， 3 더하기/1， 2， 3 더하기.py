nlist = [-1 for _ in range(12)]
nlist[0] = 0
nlist[1] = 1
nlist[2] = 2
nlist[3] = 4

def dp(n):
    if nlist[n] != -1:
        return nlist[n]
    for i in range(4, n+1):
        nlist[i] = nlist[i-1] + nlist[i-2] + nlist[i-3]
    return nlist[n]

T = int(input())
for _ in range(T):
    print(dp(int(input())))