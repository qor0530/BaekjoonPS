N = int(input())

a, b, c = map(int, input().split())

maximum = 0

if a > N:
    maximum += N
else:
    maximum += a
if b > N:
    maximum += N
else:
    maximum += b
if c > N:
    maximum += N
else:
    maximum += c

print(maximum)

