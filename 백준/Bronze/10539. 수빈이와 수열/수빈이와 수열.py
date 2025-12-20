n = int(input())
Barr = list(map(int, input().split()))
Aarr = []

for i in range(n):
    value = Barr[i]*(i+1)
    for j in range(0, i):
        value -= Aarr[j]
    Aarr.append(value)

print(*Aarr, sep=' ')