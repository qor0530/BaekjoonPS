import math

n, game = map(str, input().split())
n = int(n)
max_player = 0

if game == 'Y':
  max_player = 1
elif game == 'F':
  max_player = 2
elif game == 'O':
  max_player = 3

namelist = []
checklist = []
count = 0

for i in range(n):
  namelist.append(input())

count = len({n: 0 for n in namelist})
play_count = math.floor(count / max_player)

print(play_count)
