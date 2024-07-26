P, K = map(int, input().split())
p, q = 1, 1

for i in range(2, K+1):
    if P % i == 0:
        p = P // i
        q = i
        break
else:
    print("GOOD")
    exit()

if p >= K and q >= K:
    print("GOOD")
elif p < q:
    print("BAD", p)
else:
    print("BAD", q)