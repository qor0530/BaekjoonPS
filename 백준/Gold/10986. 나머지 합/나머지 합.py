

n, m = map(int, input().split())

seq = list(map(int, input().split()))

count = 0
num = 0

s_seq = {}
for i in range(n):
    num = (num + seq[i]) % m
    if num == 0:
        count += 1
    try:
        s_seq[num] += 1
    except:
        s_seq[num] = 1

for key, value in s_seq.items():
    if value >= 2:
        count += (value * (value-1)) / 2
print(int(count))