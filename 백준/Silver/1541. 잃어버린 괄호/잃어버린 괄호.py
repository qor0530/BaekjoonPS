import sys
input = sys.stdin.readline

string = input().rstrip()
nlist = []
chr = ''
for s in string:
    if s == '+' or s == '-':
        if chr != '':
            nlist.append(chr)
            chr = ''
        nlist.append(s)
    else:
        chr += s
if chr != '':
    nlist.append(chr)

minusnum = 0
sum = 0
minusOn = False
for n in nlist:
    if n == '-':
        minusOn = True
        sum -= minusnum
        minusnum = 0
    elif n == '+':
        # minusOn = False
        pass
    else:
        if minusOn:
            minusnum += int(n)
        else:
            sum += int(n)
sum -= minusnum
print(sum)