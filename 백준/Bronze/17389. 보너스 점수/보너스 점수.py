n = int(input())
string = input()

score = 0
bonus = 0

for i in range(n):
    if string[i] == 'O':
        score += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)