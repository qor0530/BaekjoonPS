N, M , K = map(int, input().split())

count = 0
result = "-1"

for i in range(M):
    x, y = map(int, input().split())
    count += y
    if count > K and result == "-1":
        result = str(i+1)+ " 1" 
        
print(result)