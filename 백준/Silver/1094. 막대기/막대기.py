X = int(input())
stick = [64]
result = sum(stick)
while X != result:
    poped = stick.pop()//2
    stick.append(poped)
    result = sum(stick)
    if  X > result:
        stick.append(stick[-1])
    else:
        pass
    result = sum(stick)
print(len(stick))