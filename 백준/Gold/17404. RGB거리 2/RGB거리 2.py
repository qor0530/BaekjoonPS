from collections import deque
n = int(input())
graph = deque()
result = float('inf')
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(3):
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(n)]
    dp[0][i] = graph[0][i]
    for j in range(1, n):
        dp[j][0] = graph[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = graph[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = graph[j][2] + min(dp[j-1][1], dp[j-1][0])
    for k in range(3):
        if i != k:
            result = min(result, dp[-1][k])

print(result)