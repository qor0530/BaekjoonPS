from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

n, r, q = map(int, input().split())

connect = defaultdict(list)

for i in range(n-1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

child = [[] for i in range(n+1)]
parent = [-1 for i in range(n+1)]

def makeTree(currentNode, mom):
    for Node in connect[currentNode]:
        if Node != mom:
            child[currentNode].append(Node)
            parent[Node] = currentNode
            makeTree(Node, currentNode)

makeTree(r, -1)

size = [0 for i in range(n+1)]

def countSubtreeNodes(currentNode):
    if size[currentNode] == 0:
        size[currentNode] = 1
        for Node in child[currentNode]:
            countSubtreeNodes(Node)
            size[currentNode] += size[Node]

for i in range(q):
    now = int(sys.stdin.readline())
    countSubtreeNodes(now)
    print(size[now])