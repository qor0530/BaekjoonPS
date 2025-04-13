def solution(array, commands):
    answer = []
    for start, end, number in commands:
        cutting = sorted(array[start-1:end])
        answer.append(cutting[number-1])
        
    return answer