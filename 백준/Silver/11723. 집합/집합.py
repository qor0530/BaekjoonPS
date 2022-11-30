import sys
input = sys.stdin.readline
n = int(input())
S = 0
for _ in range(n):
    string = input().rstrip()
    if string == 'all' or string == 'empty':
        if string == 'all': S = (1 << 21) - 1
        if string == 'empty': S = 0
    else:
        response, num = string.split()
        num = int(num)
        if response == 'add':
            S |= (1 << num)
        elif response == 'remove':
            S &= ~(1 << num)
        elif response == 'check':
            print(1 if S & (1 << num) != 0 else 0)
        elif response == 'toggle':
            S ^= (1 << num)