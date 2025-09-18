road = input()

r = road.find("@")
b = road.find("#")
d = road.find("!")
count = 0
if r <= b <= d:
    while b != d:
        r += 1
        if b == r:
            b += 1
        count += 1
    print(count)
elif d <= b <= r:
    while b != d:
        r -= 1
        if b == r:
            b -= 1
        count += 1
    print(count)
else:
    print(-1)