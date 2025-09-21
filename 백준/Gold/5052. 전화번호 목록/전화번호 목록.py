t = int(input())

for _ in range(t):
    n = int(input())
    book = []
    for i in range(n):
        book.append(input())
    book.sort()
    now = book[0]
    is_match = False
    for i in range(1, n):
        if now == book[i][:len(now)]:
            is_match = True
        now = book[i]
    if is_match:
        print("NO")
    else:
        print("YES")