n = list(map(int,input().split()))
result = list(map(lambda x : n[x]**2, range(len(n))))
print(sum(result) % 10)