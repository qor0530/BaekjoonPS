n, k = map(int, input().split())
Alist = list(map(int, input().split()))
sorted_list = sorted(Alist)
Adict = {}

for i, l in enumerate(Alist):
    Adict[l] = i

for i in range(n - 1, -1, -1): #n-1 ~ 0
    if sorted_list[i] != Alist[i]:
        temp = [Alist[i], sorted_list[i]]
        Alist[i], Alist[Adict[sorted_list[i]]] = Alist[Adict[sorted_list[i]]], Alist[i]
        Adict[temp[0]], Adict[temp[1]] = Adict[temp[1]], Adict[temp[0]]
        k -= 1
        if k == 0:
            print(*temp)
            break
if k > 0:
    print(-1)