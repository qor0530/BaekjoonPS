import sys
input = sys.stdin.readline

n = int(input())

task = []
score = 0
for i in range(n):
    workshop = list(map(int, input().split()))
    if workshop[0] == 0:
        if task:
            if task[-1][1] - 1 == 0:
                score += task[-1][0]
                task.pop()
            else:
                task[-1][1] -= 1
    else:
        task.append(workshop[1:])
        if task[-1][1] - 1 == 0:
            score += task[-1][0]            
            task.pop()
        else:
            task[-1][1] -= 1

print(score)