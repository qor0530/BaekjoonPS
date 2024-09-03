N = int(input())
A = list(map(int, input().split()))
NGE = [-1] * N
stack = []
for i in range(N):
    if not stack:
        stack.append((A[i], i))
    else:
        while stack and stack[-1][0] < A[i]:
            num, idx = stack.pop()
            NGE[idx] = A[i]
        stack.append((A[i], i))
print(*NGE)