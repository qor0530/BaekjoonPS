x = []
y = []

libx = {}
liby = {}

printlist = []
for i in range(3):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)
  libx[a] = 0
  liby[b] = 0

for i in range(3):
  libx[x[i]] += 1
  liby[y[i]] += 1

for i in libx:
  if libx[i] == 1:
    printlist.append(str(i))

for i in liby:
  if liby[i] == 1:
    printlist.append(str(i))

print(' '.join(printlist))