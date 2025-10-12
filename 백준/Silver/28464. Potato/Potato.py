from collections import deque
n = int(input())
potato = deque(sorted(list(map(int, input().split()))))
s = 0
p = 0
for i in range(n):
    if i % 2 == 0:
        p += potato.pop()
    else:
        s += potato.popleft()

print(s, p)