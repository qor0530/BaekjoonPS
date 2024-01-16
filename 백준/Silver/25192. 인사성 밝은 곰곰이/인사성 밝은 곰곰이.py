n = int(input())

count = 0
isHello = []
for i in range(n):
    text = input()
    if text == "ENTER":
        count += len(set(isHello))
        isHello = []
    else:
        isHello.append(text)
count += len(set(isHello))
print(count)



