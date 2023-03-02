import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
nlist = [n]
if n == 1:
    loop = False
else:    
    loop = True
while loop:
    cnt+=1
    newlist = []
    for num in nlist:
        if num % 3 == 0:
            if int(num/3) == 1:
                loop = False
            newlist.append(int(num/3))
        if num % 2 == 0:
            if int(num/2) == 1:
                loop = False
            newlist.append(int(num/2))
        if num - 1 >= 1:
            if int(num-1) == 1:
                loop = False
            newlist.append(num-1)
    nlist = newlist

print(cnt)