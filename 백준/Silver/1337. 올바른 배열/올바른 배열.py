n = int(input())
nlist = []
for i in range(n):
    nlist.append(int(input()))
nlist.sort()
maxrange = 0
minimum = 4
count = 4
if n < 5:
    for i in range(n):
        maxrange = nlist[i] + 4
        count = 4
        for j in range(i, n):
            if nlist[j] > nlist[i] and nlist[j] <= maxrange:
                count -= 1
                if count < minimum:
                    minimum = count
else:
    for i in range(n):
        maxrange = nlist[i] + 4
        count = 4
        if i - n <= 5:
            t = n - i
        else:
            t = 5
        for j in range(i, i+t):
            if nlist[j] > nlist[i] and nlist[j] <= maxrange:
                count -= 1
                if count < minimum:
                    minimum = count
print(minimum)