n = int(input())
stick = [int(input()) for _ in range(n)]
stick.reverse()
max_length = stick[0]
count = 1
for i in range(1, n):
    if max_length < stick[i]:
        max_length = stick[i]
        count += 1

print(count)