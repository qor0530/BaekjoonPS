import sys
input = sys.stdin.readline
nlist = []
def isPrime(m):
    a = [True] * ((m*2) + 1)
    a[0] = a[1] = False
    count = 0
    for i in range(2, (m*2)+1):
        if a[i] == True:
            for j in range(i + i, (m*2)+ 1, i):
                a[j] = False

    for i in range(m+1, (m*2) + 1):
        if a[i]:
            count += 1
    return count

m = int(input())
while(m != 0):
    nlist.append(isPrime(m))
    m = int(input())

for i in range(len(nlist)):
    print(nlist[i])