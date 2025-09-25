string = input()
big = []

UCPC = "UCPC"
now = 0

for s in string:
    if  65 <= ord(s) < 65+26:
        big.append(s)
for i in range(len(big)):
    if now < 4:
            if UCPC[now] == big[i]:
                now += 1

if now == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")