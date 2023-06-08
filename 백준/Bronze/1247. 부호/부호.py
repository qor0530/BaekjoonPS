import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input().rstrip())
    result = 0
    for i in range(n):
        result += int(input().rstrip())
    if result > 0:
        print("+")
    elif result == 0:
        print(0)
    else:
        print("-")