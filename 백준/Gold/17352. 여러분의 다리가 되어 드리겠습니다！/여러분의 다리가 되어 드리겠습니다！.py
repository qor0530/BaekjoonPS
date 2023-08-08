import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
root = list(range(0, n+1))

def Find(a):
    if a != root[a]:
        return Find(root[a])
    return a

def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b
        
for _ in range(n-2):
    a, b = map(int, input().split())
    Union(a, b)
result = []
for i in range(1, n + 1):  # 부서진 다리 찾기
    if i == root[i]:
        result.append(i)
print(*result)
