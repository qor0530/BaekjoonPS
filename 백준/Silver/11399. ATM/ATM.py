from sys import stdin
input = stdin.readline
n = int(input())
sum = 0

m = list(map(int, input().split()))
m.sort()
for i in range(len(m)):
 sum += m[i]*(len(m)-i) 
print(sum)