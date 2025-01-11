import sys
input = sys.stdin.readline
print = sys.stdout.write
stack = []

def operate_1(num):
    stack.append(num)

def operate_2():
    if stack == []:
        return -1
    else:
        return stack.pop()

def operate_3():
    return len(stack)

def operate_4():
    if stack == []:
        return 1
    else:
        return 0

def operate_5():
    if stack == []:
        return -1
    else:
        return stack[-1]

N = int(input())

for i in range(N):
    command = input().split()
    if command[0] == '1':
        operate_1(int(command[1]))
    elif command[0] == '2':
        print("%d\n" % operate_2())
    elif command[0] == '3':
        print("%d\n" % operate_3())
    elif command[0] == '4':
        print("%d\n" % operate_4())
    elif command[0] == '5':
        print("%d\n" % operate_5())