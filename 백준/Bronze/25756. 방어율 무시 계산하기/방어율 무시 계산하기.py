ammorbreak = 0

n = int(input())
nlist = list(map(int, input().split()))
for i in nlist:
    ammorbreak = 1 - (1-ammorbreak) * (1-(i/100))
    print(100 * ammorbreak)
