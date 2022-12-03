N = int(input())
pibo = [0]
for i in range(1, N + 1):
    if (i == 1):
        pibo.append(1)
    else:
        pibo.append(pibo[i - 1] + pibo[i - 2])
print(pibo[N])