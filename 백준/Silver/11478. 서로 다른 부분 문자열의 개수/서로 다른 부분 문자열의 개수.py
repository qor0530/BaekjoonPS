nPr = []
n = list(input())

for i in range(len(n)):
  for j in range(len(n)):
    if j + i <= len(n):
      # for k in range(i):
      #   newstr =
      newstr = '.'.join(n[j:j + i + 1])
      nPr.append(newstr)
    else:
      break

setnPr = set(nPr)

print(len(setnPr))
