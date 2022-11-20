from sys import stdin
input = stdin.readline
n = list(input().rstrip())
count = 0 
sum = 0
for i in range(len(n)):
  sum += int(n[i]) 
if sum < 10:
    print(count)
    if sum % 3 == 0:
      print('YES')
    else:
      print('NO')
else:
  count += 1
  while 1:
    sum = 0
    for i in range(len(n)):
      sum += int(n[i])  
    if sum < 10:
      print(count)
      if sum % 3 == 0:
        print('YES')
      else:
        print('NO')
      break
    else:
      count += 1
      n = list(str(sum))
    
    
  