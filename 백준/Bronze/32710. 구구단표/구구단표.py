a = int(input())
isA = False
for i in range(2, 10):
    for j in range(1, 10):
        if a == i * j or a == i or a == j:
            isA = True 
            break

if isA:
    print('1')
else:
    print('0')