import math


W, N = map(str, input().split())

N = int(N)

nlist = []
for i in range(N):
    addlist = list(map(int, input().split()))
    nlist.append(addlist)

temp = 0
if W == 'D' or W == 'U':
    for i in range(math.floor(N/2)):
        for j in range(N):
            temp = nlist[i][j]
            nlist[i][j] = nlist[N-1-i][j]
            nlist[N-1-i][j] = temp
    for i in range(N):
        for j in range(N):
            if nlist[i][j] == 3 or nlist[i][j] == 4 or nlist[i][j] == 7 or nlist[i][j] == 6 or nlist[i][j] == 9:
                nlist[i][j] = '?' 
            elif nlist[i][j] == 2:
                nlist[i][j] = 5
            elif nlist[i][j] == 5:
                nlist[i][j] = 2

if W == 'L' or W == 'R':
    for i in range(N):
        for j in range(math.floor(N/2)):
            temp = nlist[i][j]
            nlist[i][j] = nlist[i][N - j - 1]
            nlist[i][N - j - 1] = temp
    for i in range(N):
        for j in range(N):
            if nlist[i][j] == 3 or nlist[i][j] == 4 or nlist[i][j] == 7 or nlist[i][j] == 6 or nlist[i][j] == 9:
                nlist[i][j] = '?' 
            elif nlist[i][j] == 2:
                nlist[i][j] = 5
            elif nlist[i][j] == 5:
                nlist[i][j] = 2
for i in range(N):
    print(*nlist[i])