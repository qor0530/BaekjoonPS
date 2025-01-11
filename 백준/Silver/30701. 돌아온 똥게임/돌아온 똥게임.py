N, D = map(int, input().split())

monster = []
equipment = []

for i in range(N):
    A, X = map(int, input().split())
    if A == 1:
        monster.append(X)
    else: 
        equipment.append(X)

equipment = sorted(equipment)
monster = sorted(monster)

equipment_len = len(equipment)
count = 0

for stage in range(len(monster)):
    while equipment or monster[stage] < D:
        if D > monster[stage]:
            D += monster[stage]
            count += 1
            break
        else:
            D *= equipment.pop(0)
            
print(count + equipment_len)