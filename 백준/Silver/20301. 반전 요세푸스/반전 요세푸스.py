import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
reverse = False
que = []
count = 0
for i in range(1,n + 1):
    que.append(i)

for i in range(1, n + 1):
    if not reverse:
        count += k - 1
        count %= len(que)
        num = que.pop(count)
    else:
        count -= k
        count %= len(que)
        count = abs(count)
        num = que.pop(count)
    if i % m == 0:
        reverse = not reverse
    print(num)