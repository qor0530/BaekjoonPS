n, m = map(int, input().split())

find_string = []
get_strings = []

for i in range(n):
    find_string.append(input())
for j in range(m):
    get_strings.append(input())

str_dict = {value: i for i, value in enumerate(find_string)}

for i in get_strings:
    if i.isdigit():
        print(find_string[int(i) - 1])
    else:
        print(str_dict[i] + 1)
