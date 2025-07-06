
w, k = 0, 0
w_list = []
k_list = []
for i in range(20):
    score = int(input())
    if i < 10:
        w_list.append(score)
    else:
        k_list.append(score)

w_list.sort(reverse=True)
k_list.sort(reverse=True)

print(sum(w_list[0:3]), sum(k_list[0:3]))