import sys
input = sys.stdin.readline
from collections import deque

stringlist = list(input().rstrip()) + [' ']
reList = deque([])
enterList = []
IsReverse = True
for string in stringlist:
    if string == ' ' and IsReverse:
        enterList += reList
        reList = deque([])
    if string == '<':
        IsReverse = False
        enterList += reList
        reList = deque([])
    if IsReverse and string != ' ':
        reList.appendleft(string)
    else:
        enterList.append(string)
    if string == '>':
        IsReverse = True

printstring = ''
for string in enterList:
    printstring += string
print(printstring)