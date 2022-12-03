
N, a, b = map(int, input().split())
count = 1
while N != 1:
    
    if a < b:
        if b - a == 1 and a % 2 == 1:
            break
    else:
        if a - b == 1 and b % 2 == 1:
            break
            
    if a % 2 == 0:
        a /= 2
    else:
        a += 1
        a /= 2
        a = int(a)
    if b % 2 == 0:
        b /= 2
    else:
        b += 1
        b /= 2
        b = int(b)
    if N % 2 == 0:
        N /= 2
    else:
        N += 1
        N /= 2
        N = int(N)

   
    count += 1
        
print(count)