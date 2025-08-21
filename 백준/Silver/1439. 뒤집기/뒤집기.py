s = input()

zero = 0
one = 0
before = s[0]

if before == '0':
    zero += 1
else:
    one += 1

now = 1
while now < len(s):
    if s[now] != before:
        if s[now] == '0':
            zero += 1
        else:
            one += 1
        before = s[now]
    now += 1

print(min(zero, one))