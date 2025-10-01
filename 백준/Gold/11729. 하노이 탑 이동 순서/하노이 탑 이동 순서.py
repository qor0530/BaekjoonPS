k = int(input())

def hanoi(a, b, c, n):
    if n == 1:
        return [a, b]
    else:
        return hanoi(a, c, b, n-1) + hanoi(a, b, c, 1) + hanoi(c, b, a, n-1)
    
root = hanoi(1, 3, 2, k)
length = len(root)//2
print(length)
for i in range(0, length*2, 2):
    print(root[i], root[i+1])