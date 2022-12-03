ans = []
a, b, c = map(int, input().split())
while a != 0 or b != 0 or c != 0:
  if a == 0 and b == 0 and c == 0:
    break
  if (a * a + b * b == c * c) or (a * a == b * b + c * c) or (a * a + c * c == b * b):
    ans.append("right")
  else:
    ans.append("wrong")
  a, b, c = map(int, input().split())


for i in ans:
  print(i)
