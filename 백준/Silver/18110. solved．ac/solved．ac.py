import sys

def round_custom(num):
    return int(num + 0.5)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    ops = []
    for _ in range(n):
        ops.append(int(sys.stdin.readline()))
    ops.sort()

    cut_num = round_custom(n * 0.15)
    
    if n - 2 * cut_num > 0:
        cut_ops = ops[cut_num : n - cut_num]
        average = sum(cut_ops) / len(cut_ops)
        print(round_custom(average))
    else:
        print(0)