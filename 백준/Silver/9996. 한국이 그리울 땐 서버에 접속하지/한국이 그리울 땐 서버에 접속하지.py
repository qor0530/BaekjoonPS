import re
n = int(input())
pattern = list(input())
alphabet1 = ""
alphabet2 = ""
front = True
for i in range(len(pattern)):
  if pattern[i] != "*" and front:
    alphabet1 += pattern[i]
  elif pattern[i] == "*":
    front = False
  else:
    alphabet2 += pattern[i]
    
    
p = re.compile("^{0}[a-z]*{1}$".format(alphabet1,alphabet2))
for _ in range(n):
  result = p.findall(input())
  if len(result) != 0:
    print("DA")
  else:
    print("NE")