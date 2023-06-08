from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
que = deque([])
for _ in range(n):
    command = input().split()
    try:
        if command[0] == 'push_front': que.appendleft(command[1])
        elif command[0] == 'push_back': que.append(command[1])
        elif command[0] == 'pop_front': print(que.popleft())
        elif command[0] == 'pop_back': print(que.pop())
        elif command[0] == 'size': print(len(que))
        elif command[0] == 'front': print(que[0])
        elif command[0] == 'back': print(que[-1])
        else:
            if not len(que):
                print(1)
            else:
                print(0)
    except:
        print(-1)