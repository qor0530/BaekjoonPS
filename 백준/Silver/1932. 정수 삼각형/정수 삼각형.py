n = int(input())
back = []
for i in range(n):
    que = list(map(int, input().split()))
    if i != 0:
        for j in range(i+1):
            if j-1 >= 0 and j < i:
                if back[j-1] > back[j]:
                    que[j] += back[j-1]
                else:
                    que[j] += back[j]
            elif j-1 < 0:
                que[j] += back[j]
            else:
                que[j] += back[j-1]
        back = que
    else:
        back = que
print(max(que))