import itertools

n, m = map(int, input().split())

strings = sorted(list(map(int, input().split(' '))))

dic = list(itertools.combinations_with_replacement(strings, m))
dic = sorted(list(set(dic)))
for i in range(len(dic)):
    print(*dic[i])