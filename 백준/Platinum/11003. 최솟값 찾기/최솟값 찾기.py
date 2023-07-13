from collections import deque
n, a = map(int, input().split())

nums = list(map(int, input().split()))

queue = deque([])

for i in range(n):
    if queue and queue[0][1] <= (i-a):
        queue.popleft()
    while queue:
        if queue[-1][0] >= nums[i]:
            queue.pop()
        else:
            queue.append([nums[i], i])
            break
    else:
        queue.append([nums[i], i])
    print(queue[0][0], end=' ')