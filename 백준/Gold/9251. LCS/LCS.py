import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s1 = ' ' + s1
s2 = ' ' + s2
graph = [[0] * len(s2) for i in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0:
            graph[i][j] = 0  
        elif s1[i] == s2[j]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])

print(graph[len(s1)-1][len(s2)-1])