from collections import deque
N, K = map(int, input().split())
cats = list(map(int, input().split()))
cats.sort()
count = 0
cats = deque(cats)
for i in range(N):
    try:
        first_cat = cats.popleft()
        for i in range(len(cats)):
            if first_cat + cats[len(cats)-i-1] <= K:
                cats.remove(cats[len(cats)-i-1])
                count += 1
                break
        else:
            break
    except:
        continue    
    
print(count)