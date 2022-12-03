n, m = map(int, input().split())

find_list = []
except_list = []

for i in range(n):
    find_list.append(input())
for j in range(m):
    except_list.append(input())

find_dict = {value: 0 for value in find_list}

result = []

for i in except_list:
    if i in find_dict:
        result.append(i)

print(len(result))
result.sort()

for i in result:
    print(i)
