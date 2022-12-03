import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numlist = list(map(int, input().split()))
slice = [i for i in numlist[0:m]]
sum = sum(slice)
high = sum
for i in range(m, n): 
  sum += numlist[i]
  sum -= numlist[i - m]
  if sum > high:
    high = sum
print(high)