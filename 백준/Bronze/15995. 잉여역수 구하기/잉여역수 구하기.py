a, m = map(int, input().split())
x = 1
while (a*x)%m != 1:
    x += 1
print(x)