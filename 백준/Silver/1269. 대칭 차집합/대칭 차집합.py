a, b = map(int, input().split())

alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

sumlist = alist + blist

count_dict = {}
count = 0

for i in sumlist:
  try: 
    count_dict[i] += 1
    count += 1
  except: 
    count_dict[i] = 1 

print(len(count_dict) - count)