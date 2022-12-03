import itertools

n, m = map(int, input().split())

n = [i for i in range(1, n + 1)]

nPr = itertools.product(n, repeat=m)
nPrlist = list(nPr)
for i in range(len(nPrlist)):
  numstr = ''
  for j in range(m):
    numstr += str(nPrlist[i][j]) + ' '
  print(numstr)
