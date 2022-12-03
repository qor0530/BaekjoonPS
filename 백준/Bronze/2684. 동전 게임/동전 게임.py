penny = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]
P = int(input())

for i in range(P):
    test = input()
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(38):
        for k in range(8):
            if (test[j:j + 3] == penny[k]):
                count[k] += 1
    print(*count)
