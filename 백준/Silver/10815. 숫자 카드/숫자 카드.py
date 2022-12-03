from sys import stdin

n = int(stdin.readline())
nlist = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
mlist = list(map(int, stdin.readline().split()))
nlist.sort()

mdict = {value: 0 for value in mlist}

for i in nlist:
    if i in mdict:
        mdict[i] = 1

cardchar = ""
for i in mlist:
    cardchar += f"{mdict[i]} "
print(cardchar)
