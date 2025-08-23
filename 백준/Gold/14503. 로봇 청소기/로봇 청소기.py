n, m = map(int, input().split())
x, y, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

count = 0

paths = [(-1, 0), (0, 1), (1, 0), (0, -1)]
Playing = True
while Playing:
    if room[x][y] == 0:
        count += 1
        room[x][y] = 2
    else:
        cleaning = False
        for a, b in paths:
            nx, ny = x+a, y+b
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if room[nx][ny] == 0:
                    cleaning = True
                    break
        if cleaning:
            d = (d+3)%4
            if room[x + paths[d][0]][y + paths[d][1]] == 0:
                x += paths[d][0]
                y += paths[d][1]
        else:
            nx, ny = x+paths[(d+2)%4][0], y+paths[(d+2)%4][1]
            if room[nx][ny] != 1:
                x, y = nx, ny
            else:
                Playing = False

print(count)
