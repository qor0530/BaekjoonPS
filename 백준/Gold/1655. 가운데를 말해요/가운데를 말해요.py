import sys, heapq
input = sys.stdin.readline
n = int(input())
max_heap = [] #-붙여서 나왔다 들어갔다 해야함
min_heap = [] 
for i in range(n):
    num = int(input())
    if len(max_heap) <= len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if len(max_heap) >= 1 and len(min_heap) >= 1:
        if -max_heap[0] > min_heap[0]:
            swap1 = heapq.heappop(min_heap)
            swap2 = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -swap1)
            heapq.heappush(min_heap, swap2)
    print(-max_heap[0])