n, x = map(int, input().split())
days = list(map(int, input().split()))
maximum = 10000000001
for i in range(n-1):
    maximum = min(maximum, days[i]*x + days[i+1]*x)

print(maximum)