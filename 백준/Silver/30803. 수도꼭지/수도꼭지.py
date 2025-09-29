import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = list(map(int, input().split()))
toggle = [True] * n
q = int(input().rstrip())
water = sum(a)
print(water)

for i in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        _, idx, x = cmd
        idx -= 1
        if toggle[idx]:
            water -= a[idx]
            a[idx] = x
            water += a[idx]
        else:
            a[idx] = x
    else:
        _, idx = cmd
        idx -= 1
        if toggle[idx]:
            water -= a[idx]
            toggle[idx] = False
        else:
            water += a[idx]
            toggle[idx] = True
    print(water)