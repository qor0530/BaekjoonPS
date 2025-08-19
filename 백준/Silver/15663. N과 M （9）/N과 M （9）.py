import itertools

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

com = sorted(list(set(itertools.permutations(arr, M))))

for i in range(len(com)):
    print(*com[i])