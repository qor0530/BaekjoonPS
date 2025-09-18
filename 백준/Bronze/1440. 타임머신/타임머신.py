from itertools import permutations

a, b, c = map(int, input().split(":"))

def is_valid(h, m, s):
    return (1 <= h <= 12) and (0 <= m <= 59) and (0 <= s <= 59)

count = 0
for h, m, s in permutations([a, b, c], 3):
    if is_valid(h, m, s):
        count += 1

print(count)
