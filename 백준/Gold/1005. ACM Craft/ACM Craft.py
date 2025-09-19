from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

T = int(input().strip())

def max_distance(node):
    if dp[node] != -1:
        return dp[node]
    
    max_cost = 0
    for child in direct[node]:
        max_cost = max(max_cost, max_distance(child))
    dp[node] = max_cost + d[node]
    return dp[node]

results = []

for _ in range(T):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    direct = defaultdict(list)

    for _ in range(k):
        x, y = map(int, input().split())
        direct[y].append(x)  

    w = int(input())
    dp = [-1] * (n+1)

    results.append(max_distance(w))

print(*results, sep='\n')
