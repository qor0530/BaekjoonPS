n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

if n >= 3:
    a = []
    graph[0][0] = (graph[0][1] + graph[0][2] - graph[1][2])//2
    a.append(graph[0][0])
    for i in range(1, n):
        graph[i][i] = graph[i-1][i] - graph[i-1][i-1]
        a.append(graph[i][i])
    print(*a, sep=' ')
else:
    x = graph[0][1]//2
    print(x, x)