n, m = map(int, input().split())

m_str = list(input())
for i in range(m):
    now = 0
    string = list(input())
    for s in string:
        if now < n:
            if s == m_str[now]:
                now += 1
    if now == n:
        print("true")
    else:
        print("false")