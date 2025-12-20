n = int(input())

graph = [[0]* 1001 for _ in range(1001)]

for i in range(n):
    x1, y1, wi, he = map(int, input().split())
    for x in range(x1, x1+wi):
        for y in range(y1, y1+he):
            graph[x][y] = i+1

result = [0] * (n+1)
for i in range(1001):
    for j in range(1001):
        if graph[i][j] != 0:
            result[graph[i][j]] += 1

print('\n'.join(map(str, result[1:])))