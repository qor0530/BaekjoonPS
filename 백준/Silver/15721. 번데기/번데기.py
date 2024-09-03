players = int(input())
target_num = int(input())
target_shape = int(input())
count = 0
now = 0
n = 2
def check_target(n, target):
  if n == target:
    return True
  else:
    return False
while True:
    games = [0, 1, 0, 1, *([0] * n), *([1] * n)]
    for game in games:
        if target_shape == game:
            count += 1
            if check_target(count, target_num):
                break
        now += 1
        now %= players
    n+=1
    if check_target(count, target_num):
        break
print(now)