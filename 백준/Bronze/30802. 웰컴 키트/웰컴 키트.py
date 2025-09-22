n = int(input())
applier = list(map(int, input().split()))
t, p = map(int, input().split())

tc = 0
for i in range(6):
    while applier[i] > 0:
        applier[i] -= t
        tc += 1

print(tc)
print(n//p, n%p)