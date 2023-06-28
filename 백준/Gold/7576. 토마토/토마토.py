def get_surroundPos(field, pos, MW, MH):
    rPos = []
    if pos[0] - 1 >= 0:
        if field[pos[0]-1][pos[1]] == 0:
            rPos.append((pos[0]-1, pos[1]))
            field[pos[0]-1][pos[1]] = 1
    if pos[0] + 1 < MH:
        if field[pos[0]+1][pos[1]] == 0:
            rPos.append((pos[0]+1, pos[1]))
            field[pos[0]+1][pos[1]] = 1
    if pos[1] - 1 >= 0:
        if field[pos[0]][pos[1]-1] == 0:
            rPos.append((pos[0], pos[1]-1))
            field[pos[0]][pos[1]-1] = 1
    if pos[1] + 1 < MW:
        if field[pos[0]][pos[1]+1] == 0:
            rPos.append((pos[0], pos[1]+1))
            field[pos[0]][pos[1]+1] = 1
    return rPos, field

w, h = map(int, input().split())
field = []
underripe_tomato = []
for _ in range(h):
    field.append(list(map(int, input().split(' '))))
for i in range(h):
    for j in range(w):
        if field[i][j] == 1:
            underripe_tomato.append((i, j)) #pos == 리스트로 봤을때랑 같음
unripe_tomato = []
for pos in underripe_tomato:
        rPos, field = get_surroundPos(field, pos, w, h)
        unripe_tomato += rPos
underripe_tomato = list(set(unripe_tomato))
tries = 0
while underripe_tomato:
    unripe_tomato = []
    for pos in underripe_tomato:
        rPos, field = get_surroundPos(field, pos, w, h)
        unripe_tomato += rPos
    underripe_tomato = list(set(unripe_tomato))
    tries += 1
for i in range(h):
    for j in range(w):
        if field[i][j] == 0:
            tries = -1
print(tries)