n, k = map(int, input().split())
days = list(map(int, input().split()))
m = -99999999999
for i in range(n-k+1):
    s = 0
    for j in range(i, i+k):
        s += days[j]
    if m < s:
        m = s
print(m)