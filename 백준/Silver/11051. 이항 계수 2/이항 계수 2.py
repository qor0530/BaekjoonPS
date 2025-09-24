n, k = map(int, input().split())

# n!//k!(n-k)!
dp = [-1 for _ in range(1001)]
def factorial(num):
    if dp[num] != -1:
        return dp[num]
    elif num > 1:
        dp[num] = factorial(num-1) * num
        return dp[num]
    else:
        return 1
print((factorial(n) // (factorial(k) * factorial(n-k)))% 10007)