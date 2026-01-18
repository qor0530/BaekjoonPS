n, l = map(int, input().split())
now = 0
count = 0
l = str(l)
while count < n:
    now += 1
    if l not in list(str(now)):
        count += 1
  
print(now)