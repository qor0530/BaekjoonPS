grade = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}

n = int(input())
hg = 0
score = 0.0

for i in range(n):
    line = input().split()
    hg += float(line[1])
    score += float(line[1]) * grade[line[2]]

result = score / hg

result = round(result, 3)
if str(result)[-1] == "5" and len(str(result).split(".")[1]) == 3:
    result = round(result, 2) + 0.01
else:
    result = round(result, 2)
print(f"{result:.2f}")