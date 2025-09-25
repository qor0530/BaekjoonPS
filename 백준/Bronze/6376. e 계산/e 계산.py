n = 0
e = 1

def fac(a):
    if a == 1:
        return 1
    return fac(a-1) * a

print("""n e
- -----------""")
for _ in range(10):

    if int(e) == e:
        e = int(e)
        print(f"{n} {e}")
    else:
        if n != 8:
            print(f"{n} {round(e, 9)}")
        else:
            print(f"{n} {round(e, 9)}0")
    n += 1
    e = round(e + 1/fac(n), 10)
