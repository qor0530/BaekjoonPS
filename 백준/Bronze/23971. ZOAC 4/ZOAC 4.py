h, w, n, m = map(int, input().split())

hcount = h // (n+1)
wcount = w // (m+1)

if h % (n+1) != 0:
    hcount += 1

if w % (m+1) != 0:
    wcount += 1

print(hcount * wcount)