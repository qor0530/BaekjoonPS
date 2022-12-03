graph = {
    'black': [0, 1],
    'brown': [1, 10],
    'red': [2, 100],
    'orange': [3, 1000],
    'yellow': [4, 10000],
    'green': [5, 100000],
    'blue': [6, 1000000],
    'violet': [7, 10000000],
    'grey': [8, 100000000],
    'white': [9, 1000000000]
}
register = 0
for i in range(3):
    color = input()
    if (i == 0):
        register += graph[color][0] * 10
    elif (i == 1):
        register += graph[color][0]
    else:
        register *= graph[color][1]
print(register)