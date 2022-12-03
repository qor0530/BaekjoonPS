N = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort(reverse = True)
sum = 0
for i in range(N):
    sum += A[i] * B[i]
    
print(sum)