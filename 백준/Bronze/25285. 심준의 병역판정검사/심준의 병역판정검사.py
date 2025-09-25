t = int(input())

def bmi(cm, kg):
    return kg/((cm / 100)**2)

for _ in range(t):
    cm, kg = map(int, input().split())
    if cm < 140.1:
        print(6)
    elif cm < 146:
        print(5)
    elif cm < 159:
        print(4)
    elif cm < 161:
        if 16 <= bmi(cm, kg) < 35:
            print(3)
        else:
            print(4)
    elif cm < 204:
        if 16 > bmi(cm, kg) or 35 <= bmi(cm, kg):
            print(4)
        elif 16 <= bmi(cm, kg) < 18.5 or 30 <= bmi(cm, kg) < 35:
            print(3)
        elif 18.5 <= bmi(cm, kg) < 20 or 25 <= bmi(cm, kg) < 30:
            print(2)
        else:
            print(1)
    else:
        print(4)