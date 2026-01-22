n = int(input())
while n != 0:
    count = 0
    for i in range(1, n+1):
        count += i*i
    print(count)
    n = int(input())
