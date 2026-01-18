n = int(input())
count = 0
for i in range(n):
    T = list(map(int, input().split()))
    is_solved = True
    t = 0
    if T[0] == T[1] == T[2] == -1:
        is_solved = False
    else:
        try:
            a = T.index(-1)
            for i in range(a, 3):
                if T[i] != -1:
                    is_solved = False
            if T[:a] != sorted(T[:a]):
                is_solved = False
        except: 
            if T != sorted(T):
                is_solved = False
        
    if is_solved:
        count += 1
    
print(count)