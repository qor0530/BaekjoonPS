def eraze(a):
    a /= 100
    a = int(a)
    a *= 100
    return a


N = int(input())
N = eraze(N)
F = int(input())
for i in range(0, 99):
    if ((N + i) % F == 0):
        i = format(i, '02')
        print(i)
        break
