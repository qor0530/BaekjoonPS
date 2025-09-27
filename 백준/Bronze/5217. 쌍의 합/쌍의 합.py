t = int(input())

for i in range(t):
    n = int(input())
    pair = []
    for i in range(1, n//2+1):
        if n - i >= 0 and i != n-i:
            pair.append((i, n-i))

    print(f"Pairs for {n}: ", end='')
    for j in range(len(pair)): 
        a, b = pair[j]
        print(f"{a} {b}", end='')
        if j != len(pair)-1:
            print(", ", end='')
    print()