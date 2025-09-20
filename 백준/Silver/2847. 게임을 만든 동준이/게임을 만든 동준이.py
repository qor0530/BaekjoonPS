from collections import deque
n=int(input())
que = deque()
for i in range(n):
    que.appendleft(int(input()))
count = 0
now = que[0]
for i in range(1, n):
    while now <= que[i]:
        que[i] -= 1
        count += 1
    now = que[i]
print(count)