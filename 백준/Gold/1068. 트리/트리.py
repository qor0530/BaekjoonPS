from collections import deque, defaultdict

n = int(input())

seq = list(map(int, input().split()))
e = int(input())

tree = defaultdict(list)
dfs = deque()
for i in range(n):
    if i != e and seq[i] != e:
        if not seq[i] == -1:
            tree[seq[i]].append(i)
        else:
            dfs.append(i)
        
count = 0
while dfs:
    num = dfs.popleft()
    if tree[num]:
        for i in range(len(tree[num])):
            if tree[num][i] != e:
                dfs.append(tree[num][i])
    else:
        count += 1
print(count)