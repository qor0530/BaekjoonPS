n = int(input())

for i in range(n):
    count = 0
    life = list(input())
    for j in range(len(life)):
        if life[j] != ' ':
            count += ord(life[j]) - 64
    if count != 100:
        print(count)
    else:
        print('PERFECT LIFE')