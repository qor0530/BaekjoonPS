import sys
sys.getrecursionlimit = 1000000

N = int(input())

def nCr(n, r):
    return (fac(n) // fac(r)) // fac(n-r) 

def fac(num):
    if num <= 1: return 1
    return fac(num - 1) * num

for i in range(N):
    a, b = map(int, input().split())
    print(nCr(b, a))