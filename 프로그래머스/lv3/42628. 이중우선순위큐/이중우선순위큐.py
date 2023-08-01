import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        else:
            try:
                if num == 1 and max_heap != []:  #최댓값 삭제
                    maximum = heapq.heappop(max_heap)
                    if len(min_heap) > 0:
                        min_heap.remove(-maximum)
                if num == -1 and min_heap != []: #최솟값 삭제
                    minimum = heapq.heappop(min_heap)
                    if len(max_heap) > 0:
                        max_heap.remove(-minimum)
            except:
                max_heap = []
                min_heap = []
                
    if min_heap == [] and max_heap == []:
        return [0,0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]