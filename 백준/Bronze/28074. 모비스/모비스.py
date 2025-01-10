string = input()
mobis = ['M', 'O', 'B', 'I', 'S']
is_mobis = True
for i in mobis:
    if i not in string:
        is_mobis = False
        break

if is_mobis:
    print('YES')
else:
    print('NO')