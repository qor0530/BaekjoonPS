cup = int(input())
cost = int(input())
coupons = list()
if cup >= 20:
    coupons.append(cost * 0.25)
if cup >= 15:
    coupons.append(2000)
if cup >= 10:
    coupons.append(cost * 0.1)
if cup >= 5:
    coupons.append(500)
if coupons:
    cost -= max(coupons)
if cost < 0:
    cost = 0
print(int(cost))