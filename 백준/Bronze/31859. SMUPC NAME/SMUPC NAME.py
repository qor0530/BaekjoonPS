
n, name = map(str, input().split())
first = []
count = 0
for i in range(len(name)):
    if name[i] not in first:
        first.append(name[i])
    else:
        count += 1

first += list(str(count + 4))
first = list(str(1906 + int(n))) + first
first.append("smupc_")
first.reverse()
print("".join(first))