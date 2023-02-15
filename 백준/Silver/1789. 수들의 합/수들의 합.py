import sys
input = sys.stdin.readline

n = int(input())
target = n
count = 0
num = 1
numlist = []
loop = True
while(loop):
    count+=1
    if target - num > 0:
       target -= num
    elif target - num == 0:
        loop = False
    else:
        numlist.pop(numlist.index(num - target))
        loop = False
    numlist.append(num)
    num+=1
print(len(numlist))