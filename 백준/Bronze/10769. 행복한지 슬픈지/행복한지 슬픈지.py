string = input()

happy = 0
sad = 0

for i in range(len(string)-3):
    if string[i:i+3] == ":-)":
        happy += 1
    elif string[i:i+3] == ":-(":
        sad += 1

if happy == sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")