import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True
n = int(input())
nlist = list(map(int, input().split()))
count = 0 
for i in range(n):
    if isPrime(nlist[i]):
       count += 1 
print(count)