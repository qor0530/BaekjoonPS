t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    c = 0
    nlist = [i for i in range(n+1)]

    for i in range(0, k):
        for j in range(1, n+1):
            nlist[j] += nlist[j-1]
            
    print(nlist[n])