m, n = map(int, input().split())
k = n
while m >= k:
    k *= n
k //= n
s = ''
while k != 0:
    if m == 0:
        s += '0'
    else:
        if n < 10 or (n >= 10 and (m//k) < 10):
            s += str(m // k)
            m -= (m // k) * k
        else:
            s += chr(65 + m//k - 10)
            m -= (m // k) * k
    k //= n
print(s)