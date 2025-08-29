from collections import defaultdict

k = int(input())
for i in range(k):
    bipartite = True
    graph = defaultdict(list)
    v, e = map(int, input().split())
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # group을 만들어서 0, a그룹(1) b그룹(2)을 만듬
    # 1번 노드부터 순환, 연결된 모든 노드의 그룹이 없다면 반대 그룹으로 저장. 
    # 있다면 현재 노드와 반대인지 확인
    # 더 이상 연결된 노드가 없다면 2번 노드 확인 -> end
    group = defaultdict(int) 
    visited = set()
    for i in range(1, v+1):
        if group[i] == 0:
            group[i] = 1
            dfs = [i]
            while dfs:
                node = dfs.pop()
                now = group[node]
                visited.add(node)
                for go in graph[node]:
                    if go not in visited and group[go] != group[node]:
                        dfs.append(go)
                        if now == 1:
                            group[go] = 2
                        else:
                            group[go] = 1
                    if group[node] == group[go]:
                        bipartite = False
    if bipartite:
        print("YES")
    else:
        print("NO")