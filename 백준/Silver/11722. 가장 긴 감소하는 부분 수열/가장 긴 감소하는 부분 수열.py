n = int(input())
A = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    count = 0
    for j in range(i):
        if dp[j] > count and A[j] > A[i]: #이전 것들 중에 현재보다 작으면서 DP가 높은 것 찾기
            count = dp[j]
    dp[i] = count + 1

print(sorted(dp)[-1])