n = int(input())

graph = [["*"] * n for i in range(n)]

now = n
while now != 1:
    now //= 3
    for i in range(n):
        for j in range(n):
            if now <= i%(now*3) < now * 2 and now <= j%(now*3)< now*2:
                graph[i][j] = ' '

for i in range(n):
    print(*graph[i], sep='')
