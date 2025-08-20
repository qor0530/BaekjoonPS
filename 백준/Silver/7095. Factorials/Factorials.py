n = int(input())
fac = 1
now = 1
ten = 0
appr = []
while ten <= n:
    fac = fac * now 
    while fac >= 10:
        fac /= 10
        ten += 1
    if ten == n-1:
        appr.append(now)
    now += 1
if appr:
    print(len(appr))
    print(*appr, sep='\n')
else:
    print("NO")