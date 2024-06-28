n, m = map(int, input().split())
count = 0
count += n
while n >= m:   
    count += n//m
    n = n//m
print(count)
