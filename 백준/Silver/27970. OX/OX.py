string = list(input())
count = 0
for i in range(len(string)):
    if string[i] == 'O':
        count += ((2**i) % 1000000007)
print(count % 1000000007)