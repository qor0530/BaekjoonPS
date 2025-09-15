n = int(input())

mirror = [list(input()) for _ in range(n)]

state = int(input())

if state == 1:
    for i in range(n):
        for j in range(n):
            print(mirror[i][j], end="")
        print()
elif state == 2:
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(mirror[i][j], end="")
        print()
elif state == 3:
    for i in range(n):
        for j in range(n):
            print(mirror[n - i - 1][j], end="")
        print()
else:
    pass