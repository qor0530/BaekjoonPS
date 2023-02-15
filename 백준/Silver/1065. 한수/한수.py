import sys
input = sys.stdin.readline

n = int(input())
count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
    else:
        numlist = list(f'{i}')
        diff = 0
        diff = int(numlist[0]) - int(numlist[1])
        if diff == int(numlist[1]) - int(numlist[2]):
            count+=1
print(count)