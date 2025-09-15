h = input()
n = input()
no = len(n)
count = 0
for i in range(len(h)-no+1):
    if n == h[i:i+no]:
        count += 1

print(count)