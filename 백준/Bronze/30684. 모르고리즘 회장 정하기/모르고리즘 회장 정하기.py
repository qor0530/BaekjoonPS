n = int(input())
nl = [input() for _ in range(n)]

sorted_nl = sorted(nl)
for num in sorted_nl:
    if len(num) == 3:
        print(num)
        break