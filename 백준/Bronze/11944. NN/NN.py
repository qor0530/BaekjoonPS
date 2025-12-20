n, m = input().split()
m = int(m)
string = n * int(n)
if m > len(string):
    print(string)
else:
    print(string[:m])