n, k = map(int, input().split())
w, v = [], []
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

# dp[i][j] : i번째 물건까지 고려했을 때, 배낭 무게 j에서 최대 가치
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):  # 물건 1~n
    for j in range(1, k+1):  # 배낭 무게 1~k
        if w[i-1] <= j:  # 현재 물건을 넣을 수 있으면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w[i-1]] + v[i-1])
        else:  # 못 넣으면
            dp[i][j] = dp[i-1][j]

print(dp[n][k])  # 최대 가치 출력