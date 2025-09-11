x, y, z = map(int, input().split())

while x != 0:
    if max(x, y, z) >= x + y + z - max(x, y, z):
        print("Invalid")
    else:
        if x == y == z:
            print("Equilateral")
        elif x==y or y == z or z == x:
            print("Isosceles")
        else:
            print("Scalene")
    x, y, z = map(int, input().split())
