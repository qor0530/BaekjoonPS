import itertools

n = input()
list_47 = '47'
result = []
for i in range(1, len(n)+1):
    result += list(itertools.product(list_47, repeat=i))
result = [int(''.join(x)) for x in result]
max_num = -1
for num in result:
    if num <= int(n) and num >= max_num:
        max_num = num

print(max_num)