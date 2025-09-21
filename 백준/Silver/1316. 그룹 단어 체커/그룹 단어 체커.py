n = int(input())

count = 0

for i in range(n):
    visited = set()
    s = list(input())
    while s:
        a = s.pop()
        if a not in visited:
            try:
                while s[-1] == a:
                    s.pop()
            except:
                pass
            visited.add(a)
        else:
            s.append(a)
            break
    if s == []:
        count += 1
print(count)