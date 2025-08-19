price =[350.34, 230.90, 190.55, 125.30, 180.90]

N = int(input())
for i in range(N):
    order = list(map(int, input().split()))
    bill = 0
    for j in range(5):
        bill += order[j] * price[j]

    print("${:.2f}".format(bill))
