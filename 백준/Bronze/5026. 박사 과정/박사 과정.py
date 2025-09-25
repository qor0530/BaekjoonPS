t=int(input())

for _ in range(t):
    s = input()
    if "+" in s:
        x, y = map(int, s.split('+'))
        print(x+y)
    else:
        print("skipped")