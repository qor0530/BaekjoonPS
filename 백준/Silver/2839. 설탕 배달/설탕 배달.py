import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
ifcnt = []

while n > 0:
    if n % 5 == 0:
        ifcnt.append(cnt + n//5)
    if n % 3 == 0:
        ifcnt.append(cnt + n//3)
    if n - 5 >= 0:
        n -= 5
        cnt+=1
    else:
        if n - 3 >= 0:
            n -= 3
            cnt+=1
        else:
            n -= 3
            cnt = 5000
            ifcnt.append(-1)

if len(ifcnt) == 1 and ifcnt[0] == -1:
    print(-1)
else:
    for i in ifcnt:
        if cnt > i and i != -1:
            cnt = i
    print(cnt)