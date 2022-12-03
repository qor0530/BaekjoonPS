n, m = map(int, input().split())

find_string = []
get_strings = []

for i in range(n):
  find_string.append(input())
for j in range(m):
  get_strings.append(input())

str_dict = {value:0 for value in find_string}

count = 0
for i in get_strings:
  if i in str_dict:
    count += 1

print(count)
