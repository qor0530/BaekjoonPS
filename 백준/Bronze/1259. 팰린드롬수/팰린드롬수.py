s = int(input())
while s != 0:
    s = list(str(s))
    rs = list(reversed(s))
    if s == rs:
        print("yes")
    else:
        print("no")
    s = int(input())
    