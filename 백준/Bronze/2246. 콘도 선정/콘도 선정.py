condo_d = []
condo_c = []
count = 0
n = int(input())

for i in range(n):
    d,c = map(int, input().split())
    condo_d.append([d, c])
    condo_c.append([c, d])

condo_c.sort()
condo_d.sort()

best = []

for i in range(n):
    isCondo = True
    nd, nc = condo_d[i]
    for j in range(i):
        if j != i:
            if condo_d[j][1] <= nc:
                isCondo = False
                break
    if isCondo:
        best.append([nd, nc])


for i in range(n):
    isCondo = True
    nc, nd = condo_c[i]
    for j in range(i):
        if j != i:
            if condo_c[j][1] <= nd:
                isCondo = False
                break
    if isCondo and [nd, nc] in best:
        count += 1


print(count)