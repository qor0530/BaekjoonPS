from collections import deque
T = int(input())
ans = []
for _ in range(T):
  reverse_on = False
  try:
    p = list(input())
    arr_range = int(input())
    arr = input()
    arr = arr[1:-1]
    if not arr:
      pass
    else:
      arr = list(map(int,arr.split(',')))
    deque_arr = deque(arr)
    for i in p:
      if i == 'R':
        reverse_on = not reverse_on
      if i == 'D':
        if reverse_on:
          deque_arr.pop()
        else:
          deque_arr.popleft()
    if reverse_on: 
      deque_arr.reverse()
    arr = list(deque_arr)
    str_arr = str(arr).replace(' ', '')
    ans.append(str_arr)
  except:
    ans.append("error")

for _ in ans:
  print(_)