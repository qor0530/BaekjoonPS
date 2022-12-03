num = input()
numlength = len(num)
num = int(num)
while (num != 0):
    sum = 1 + numlength
    while (num >= 1):
        if (num % 10 == 1):
            sum += 2
        elif (num % 10 == 0):
            sum += 4
        else:
            sum += 3
        num /= 10
        num = int(num)
    print(sum)
    num = input()
    numlength = len(num)
    num = int(num)
