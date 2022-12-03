import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for i in range(n+1)] for j in range(n+1)] 
def dfs(start_v, used_list):
  used_list.append(start_v)
  for i in range(n+1):
    if graph[start_v][i] == 1 and i not in used_list:
      used_list = dfs(i, used_list)
  return used_list
  
m = int(input())
for _ in range(m):
  x,y = map(int, input().split())
  graph[x][y] = graph[y][x] = 1

print(len(dfs(1, [])) - 1)


  