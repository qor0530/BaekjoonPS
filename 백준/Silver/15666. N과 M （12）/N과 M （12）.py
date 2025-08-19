import itertools

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

com = sorted(list(set(itertools.combinations_with_replacement(arr, M))))

for i in range(len(com)):
    print(*com[i])
 