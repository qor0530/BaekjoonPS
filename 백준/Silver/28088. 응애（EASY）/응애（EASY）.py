N, M, K = map(int, input().split())
cry = 0b0
for _ in range(M):
    cry |= 1 << int(input())
for _ in range(K):
    # print(bin(cry))
    up_cry = cry << 1
    up_cry &= ~(1 << N) #민 후 N번째 비트 없애기
    #cry의 N-1번쨰 비트가 1이면 0번째 비트 1로 만들기
    if cry & (1 << (N-1)):
        up_cry ^= (1 << 0)
    # print(bin(up_cry))
    #cry의 0번째 비트가 1이면 N-1번째 비트 1로 만들기
    down_cry = cry >> 1 
    if cry & (1 << 0):
        down_cry ^= (1 << (N-1))
    # print(bin(down_cry))
     
    cry = (up_cry) ^ (down_cry)
    # print(bin(cry))
    
count = 0
for i in range(N):
    if cry &  (1 << i):
        count+=1 
print(count)