n = int(input())
nl = list(map(int, input().split()))

for i in range(n):
    if nl[i] == 300:
        print("1", end=" ")
    elif nl[i] >=275:
        print("2", end=" ")
    elif nl[i] >=250:
        print("3", end=" ")
    else:
        print("4", end=" ")