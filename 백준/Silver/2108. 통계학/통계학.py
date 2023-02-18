import sys
input = sys.stdin.readline
import math

def arithmetic_mean(numlist, n):
    return round(sum(numlist)/n)

def median(numlist, n):
    newlist = sorted(numlist)
    return newlist[int((n-1)/2)]

def mode(numlist):
    numdict = {}
    highnum = 0
    most = []
    for i in numlist:
        try:
            numdict[i] += 1
            if highnum < numdict[i]:
                highnum = numdict[i]
        except:
            numdict[i] = 0 
    numque = sorted(numdict.items())
    for num in numque:
        if num[1] == highnum:
            most.append(num[0])
    if len(most) > 1:
        return most[1]
    else:
        return most[0]
       
def scope(numlist):
    newlist = sorted(numlist)
    return newlist[-1] - newlist[0]


n = int(input())
numlist = []
for _ in range(n):
    numlist.append(int(input()))
print(arithmetic_mean(numlist, n))
print(median(numlist, n))
print(mode(numlist))
print(scope(numlist))