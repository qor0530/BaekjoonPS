n = int(input())
book_prices = sorted(list(map(int, input().split())))

shelfs = []
count_shelf = 0

for i in range(n):
    if len(shelfs) == 0:
        count_shelf += 1
        shelfs.append(book_prices[i])
    elif book_prices[i] >= shelfs[0] * 2:
        shelfs = []
        count_shelf += 1
        shelfs.append(book_prices[i])
    else:
        shelfs.append(book_prices[i])

print(count_shelf)