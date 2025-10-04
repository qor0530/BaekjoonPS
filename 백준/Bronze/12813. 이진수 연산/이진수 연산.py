a = input()
b = input()

k = ""
for i in range(len(a)):
    if a[i] == b[i] and a[i] == '1':
        k += '1'
    else:
        k += '0'
print(k)
k = ""
for i in range(len(a)):
    if a[i] == '1' or b[i] == '1':
        k += '1'
    else:
        k += '0'
print(k)
k = ""
for i in range(len(a)):
    if a[i] != b[i]:
        k += '1'
    else:
        k += '0'
print(k)
k = ""
for i in range(len(a)):
    if a[i] == '1':
        k += '0'
    else:
        k += '1'
print(k)
k = ""
for i in range(len(b)):
    if b[i] == '1':
        k += '0'
    else:
        k += '1'
print(k)
