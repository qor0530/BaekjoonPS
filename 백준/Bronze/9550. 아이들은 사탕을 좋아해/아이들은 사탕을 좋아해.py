t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    candy = list(map(int, input().split()))
    count = 0
    for i in range(len(candy)):
        count += candy[i] // k
    print(count)