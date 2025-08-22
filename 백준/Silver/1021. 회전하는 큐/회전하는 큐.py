from collections import deque
n, m = map(int, input().split())

n_list = deque([-1 for _ in range(n)])

num = list(map(int, input().split()))
for i in range(m):
    n_list[num[i]-1] = i

count = 0
p_count = 0

while p_count != m:
    start = 0
    end = n - p_count - 1
    while n_list[start] != p_count and n_list[end] != p_count:
        if n - p_count - end > start:
            start += 1
        else: end -= 1

    if n_list[start] == p_count and start <= n - p_count - end:
        for i in range(start):
            n_list.append(n_list.popleft())
            count += 1
        n_list.popleft()
    elif n_list[end] == p_count:
        for i in range(n - p_count - end):
            n_list.appendleft(n_list.pop())
            count += 1
        n_list.popleft()
    else:
        print("조건문 잘못 설정")
    p_count += 1

print(count)