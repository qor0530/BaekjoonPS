import itertools

n, m = map(int, input().split())

strings = list(map(int, input().split(' ')))

d = list(itertools.permutations(strings, m))
d = sorted(list(set(d)))

for i in range(len(d)):
    print(*d[i])