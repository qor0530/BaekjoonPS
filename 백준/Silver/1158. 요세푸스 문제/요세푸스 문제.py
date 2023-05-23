from collections import deque

N, K = map(int, input().split())

nlist = [i for i in range(1, N+1)]
nlist = deque(nlist)
plist = []
for _ in range(N):
    for i in range(K):
        nlist.append(nlist.popleft())
    plist.append(nlist.pop())
print('<' , end='')
print(*plist , sep=', ', end='')
print('>' , end='')
