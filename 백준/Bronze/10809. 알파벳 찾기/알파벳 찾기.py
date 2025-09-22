s = list(input())

visited = [-1 for i in range(26)]

for i in range(len(s)):
    if visited[ord(s[i])-97] == -1:
        visited[ord(s[i])-97] = i
    
print(*visited, sep=' ')
