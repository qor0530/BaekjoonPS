n = int(input())
people = {}
for i in range(n):
    nameA, nameB = input().split(' ')
    if nameA not in people:
        people[nameA] = 0
    if nameB not in people:
        people[nameB] = 0
    if people[nameA] > 0:
        people[nameB] += 1
    if people[nameB] > 0:
        people[nameA] += 1
    if nameA == "ChongChong" or nameB == "ChongChong":
        people[nameA] += 1
        people[nameB] += 1
count = 0
for key in people:
    if people[key] >0:
        count += 1
print(count)
