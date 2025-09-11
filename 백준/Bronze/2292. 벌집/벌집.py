n = int(input())
k = 1
tries = 1
while n > k:
    k += tries * 6
    tries += 1

print(tries)