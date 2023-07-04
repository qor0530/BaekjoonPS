N, K = map(int, input().split())
string = list(input())
count = 0
for i in range(N):
    if string[i] == 'P':
        for j in range(-K, K+1):
            if 0 <= (i + j) and (i + j) < N:
                if string[i+j] == 'H':
                    string[i+j] = 'X'
                    count += 1
                    break
print(count)