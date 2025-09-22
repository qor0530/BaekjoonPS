t = int(input())

for _ in range(t):
    H, W, N = map(int, input().split())
    floor = 1
    room = 1
    for i in range(N):
        if i == N-1:
            print((floor)*100 + room)
        if floor < H:
            floor += 1
        else:
            room += 1
            floor %= H
            floor+=1