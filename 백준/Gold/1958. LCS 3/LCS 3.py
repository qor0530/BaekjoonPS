import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
s1 = ' ' + s1
s2 = ' ' + s2
s3 = ' ' + s3

graph = [[[0] * len(s3) for j in range(len(s2))] for i in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        for k in range(len(s3)):
            if i == 0 or j == 0 or k == 0:
                graph[i][j][k] = 0  
            elif s1[i] == s2[j] == s3[k]:
                graph[i][j][k] = graph[i-1][j-1][k-1] + 1
            else:
                graph[i][j][k] = max(graph[i-1][j][k], graph[i][j-1][k], graph[i][j][k-1])
            
            
print(graph[len(s1)-1][len(s2)-1][len(s3)-1])