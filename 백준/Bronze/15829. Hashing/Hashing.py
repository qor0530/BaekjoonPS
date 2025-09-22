n = int(input())
hashs = list(input())
hashing = 0
count = 1
for i in range(n):
    hashing += count * (ord(hashs[i])-96)
    count *= 31
    hashing %= 1234567891

print(hashing)