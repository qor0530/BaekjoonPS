n = int(input())
nlist = list(map(int, input().split()))
count = 0
rage = 0
for i in range(n):
    if nlist[i] == 0:
        rage -= 1
    else:
        rage += 1
    count += rage

print(count)