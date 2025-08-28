a = list(map(int, input().split()))
while a[0] != 0:
    leaf = 1
    for i in range(1, len(a)):
        if i % 2 == 1:
            leaf *= a[i]
        else:
            leaf -= a[i]
    print(leaf)
    a = list(map(int, input().split()))