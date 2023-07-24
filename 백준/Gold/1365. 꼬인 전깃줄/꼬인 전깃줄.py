import bisect
n = int(input())
A = [0] + list(map(int, input().split()))
dp = [0]
for i in range(1, n+1):
    count = 0
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]

print(n - (len(dp)-1))