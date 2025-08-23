from heapq import heappush, heappop

n = int(input())

min_heap = []
max_heap = []

solved = {}

for _ in range(n):
    p, l = map(int, input().split())
    heappush(min_heap, (l, p))
    heappush(max_heap, (-l, -p))
    try:
        solved[p].append(l)
    except:
        solved[p] = [l]

m = int(input())

for _ in range(m):
    cmd = input().split()
    if len(cmd) == 3:
        cmd, p, l = cmd
        p, l = int(p), int(l)
        heappush(min_heap, (l, p))
        heappush(max_heap, (-l, -p))
        try:
            solved[p].append(l)
        except:
            solved[p] = [l]
    else:
        cmd, num = cmd
        num = int(num)
        if cmd == 'recommend':
            if num == 1:
                l, p= heappop(max_heap)
                while -l not in solved[-p]:
                    l, p= heappop(max_heap)
                print(-p)
                heappush(max_heap, (l, p))
            else:
                l, p = heappop(min_heap)
                while l not in solved[p]:
                    l, p = heappop(min_heap)
                print(p)
                heappush(min_heap, (l, p))
        elif cmd == 'solved':
            solved[num].pop(0)
        else:
            pass
