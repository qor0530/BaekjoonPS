a, b = map(int, input().split())

cd = 1
cm = 1

for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        cd = i

print(cd)

now = 2

while a != 1 or b != 1:
    if a % now == 0 and b % now == 0:
        cm *= now
        a //= now
        b //= now
        now = 2
    elif a % now == 0:
        cm *= now
        a //= now
        now = 2
    elif b % now == 0:
        cm *= now
        b //= now 
        now = 2
    else:
        now += 1

print(cm)