import sys
input = sys.stdin.readline

ilist = []
maxlen = 0
for i in range(5):
    stringlist = list(input().rstrip())
    ilist.append(stringlist)
    if maxlen < len(stringlist): maxlen = len(stringlist)
string = ""
for i in range(maxlen):
    for j in range(5):
        try:
            string += ilist[j][i]
        except:
            pass

print(string)