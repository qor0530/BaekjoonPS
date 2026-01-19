A,B = map(int, input().split())
if B %2 == 1:
    B += 1
count = 0
for i in range(1, B, 2):
    if A <= i or A <= i+1:
        count += 1
    
print(count)

