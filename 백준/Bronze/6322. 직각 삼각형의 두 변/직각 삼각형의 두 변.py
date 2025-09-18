import math
a, b, c = map(int, input().split())

count = 1
while a != 0 and b != 0 and c != 0:
    print(f"Triangle #{count}")
    count += 1
    if a == -1:
        if c**2 - b**2 > 0:
            print("a = %.3f" % round(math.sqrt(c**2 - b**2), 3))
        else:
            print("Impossible.")
    elif b == -1:
        if c**2 - a**2 > 0:
            print("b = %.3f" % round(math.sqrt(c**2 - a**2), 3))
        else:
            print("Impossible.")
    else:
        print("c = %.3f " %round(math.sqrt(a**2+b**2), 3))
    a, b, c = map(int, input().split())
    print()
