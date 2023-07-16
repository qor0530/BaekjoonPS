N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]   
#LT[0], LT[1], RB[0], RB[1]
aubergine = [N//2-1, N//2-1, N//2, N//2] 
count = 0
direction = ""
while True:
    up, down, left, right = 0, 0, 0, 0
    #UP
    if (aubergine[0] - 1) >= 0:
        for i in range(aubergine[1], aubergine[3]+1):
            up += graph[aubergine[0] - 1][i]
    else:
        up = -1
    #DOWN
    if (aubergine[2] + 1) < N:
        for i in range(aubergine[1], aubergine[3]+1):
            down += graph[aubergine[2] + 1][i]
    else:
        down = -1
    #LEFT
    if (aubergine[1] - 1) >= 0:
        for i in range(aubergine[0], aubergine[2]+1):
            left += graph[i][aubergine[1] - 1]
    else:
        left = -1
    #RIGHT
    if (aubergine[3] + 1) < N:
        for i in range(aubergine[0], aubergine[2]+1):
            right += graph[i][aubergine[3] + 1]
    else:
        right = -1
    max_value = max(up, down, left, right)
    if max_value <= 0:
        break
    else:
        count += max_value
        if max_value == up:
            aubergine[0] -= 1
            direction += "U"
        elif max_value == down: 
            aubergine[2] += 1
            direction += "D"
        elif max_value == left: 
            aubergine[1] -= 1
            direction += "L"
        elif max_value == right: 
            aubergine[3] += 1
            direction += "R"
print(count)
print(direction)