N = int(input())
keep = []
for i in range(N):
    string = list(input())
    if string == keep:
        pass
    else:
        if keep != []:
            for j in range(len(string)):
                if string[j] != keep[j]:
                    keep[j] = "?"
        else:
            keep = string

print(''.join(keep))