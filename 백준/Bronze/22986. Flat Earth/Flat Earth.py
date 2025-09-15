t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if k > n:
        k = n
    result = (k + 1) * (2 * n - k) * 2
    print(result)