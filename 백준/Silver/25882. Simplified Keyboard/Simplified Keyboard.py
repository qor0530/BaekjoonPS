keyboard = []
keyboard.append(['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i'])
keyboard.append(['j','k','l','m','n','o','p', 'q', 'r'])
keyboard.append(['s','t','u','v','w','x', 'y', 'z', ' '])
w = 3
h = 9

def fk(char):
    fk_list = []
    num = ord(char) - 97
    x = num // 9
    y = num % 9
    for i in range(-1, 2):
        for j in range(-1, 2):
            ax, ay = x+i, y+j
            if 0 <= ax <w and 0<= ay <h:
                fk_list.append(keyboard[ax][ay])
    return fk_list

n = int(input())
for i in range(n):
    a, b = input().split()
    pattern = 1
    if len(a) == len(b):
        for j in range(len(a)):
            if a[j] != b[j]:
                if b[j] not in fk(a[j]):
                    pattern = 3
                else:
                    if pattern != 3:
                        pattern = 2
    else:
        pattern = 3
    print(pattern)