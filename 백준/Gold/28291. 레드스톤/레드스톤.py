W, H = map(int, input().split())
graph = [[0] * H for _ in range(W)]
N = int(input())
block = []
dust = []
lamp = []
def block_work(x, y):
    energy = 15
    graph[x][y] = energy
    if x > 0:
        graph[x-1][y] = energy
    if x+1 < W:
        graph[x+1][y] = energy
    if y > 0:
        graph[x][y-1] = energy
    if y < H-1:
        graph[x][y+1] = energy
        
def dust_work(x, y):
    energy = graph[x][y] - 1
    if x > 0 and graph[x-1][y] < energy:
        graph[x-1][y] = energy
    if x < W-1 and graph[x+1][y] < energy:
        graph[x+1][y] = energy
    if y > 0 and graph[x][y-1] < energy:
        graph[x][y-1] = energy
    if y < H-1 and graph[x][y+1] < energy:
        graph[x][y+1] = energy
for _ in range(N):
    string, x, y = input().split()
    if string == 'redstone_block':
        block.append((int(x), int(y)))
    elif string == 'redstone_dust':
        dust.append((int(x), int(y)))
    else: #redstone_lamp
        lamp.append((int(x), int(y)))
    
for x, y in block:
    block_work(x, y)

for x, y in dust:
    dust_work(x, y)

for x, y in lamp:
    if graph[x][y] == 0:
        print('failed')
        break
else:
    print('success')