n = int(input())

count = 0

for i in range(n):
    T = list(map(int, input().split()))
    while T != []:
        if T[-1] == -1:
            T.pop()
        else:
            break

            
    if T != sorted(T) or T == [] or -1 in T:
        pass
    else:
        count += 1
print(count)