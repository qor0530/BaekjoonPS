c, n = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(n)]
dp = [float('inf')] * (c + 101)
dp[0] = 0

for cost, customer in cities:
    for i in range(customer, len(dp)):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[c:]))
