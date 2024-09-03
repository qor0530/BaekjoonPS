nlist = []
sum = 0
nlist.append(int(input()))
nlist.append(int(input()))
nlist.append(int(input()))
nlist.append(int(input()))
nlist.append(int(input()))
nlist.sort()
for i in range(5):
    sum += nlist[i]
print(sum//5)
print(nlist[2])
