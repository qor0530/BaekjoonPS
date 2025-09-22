music = list(map(int, input().split()))
asc = list(range(1, 9))
dec = list(reversed(asc))
if music == asc:
    print("ascending")
elif music == dec:
    print("descending")
else:
    print("mixed")