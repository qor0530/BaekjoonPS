import sys
input = sys.stdin.readline

string = list(input().rstrip())
bracket = 0
que = []
for i in string:
    if i == ')':
        if que:
            if que[-1] == '(':
               que.pop()
            else:
                bracket+=1
        else:
            bracket+=1
    else:
        que.append('(')
bracket += len(que)

print(bracket)