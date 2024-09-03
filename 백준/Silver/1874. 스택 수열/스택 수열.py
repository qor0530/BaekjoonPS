n = int(input())
nList = [x for x in range(n, 0, -1)]
wantedList = []
for _ in range(n):
    wantedList.append(int(input()))

stack = []
history = []

for i in range(n):
    stack.append(nList.pop())
    history.append("+")
    while stack and stack[-1] == wantedList[0]:
        stack.pop()
        wantedList.pop(0)
        history.append("-")
        
if stack:
    print("NO")
else:
    for i in history:
        print(i)