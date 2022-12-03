hour, min = map(int, input().split())

l_min = int(input())

min += l_min

while min >= 60:
    min -= 60
    hour += 1

while hour >= 24:
    hour -= 24

print(hour, min)
