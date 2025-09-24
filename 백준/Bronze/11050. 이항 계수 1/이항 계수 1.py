n, k = map(int, input().split())

# n!//k!(n-k)!
dp = [-1 for _ in range(11)]
def factorial(num):
    if dp[num] != -1:
        return dp[num]
    elif num > 1:
        dp[num] = factorial(num-1) * num
        return factorial(num-1) * num
    else:
        return 1
print(factorial(n) // (factorial(k) * factorial(n-k)))