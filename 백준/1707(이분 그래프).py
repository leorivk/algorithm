import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(adj, node, color, c):
    color[node] = c
    for next in adj[node]:
        if color[next] == c:
            return False
        if color[next] == 0:
            if not dfs(adj, next, color, -c):
                return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    color = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    is_bipartite = True
    for i in range(1, v + 1):
        if color[i] == 0:
            if not dfs(adj, i, color, 1):
                is_bipartite = False
                break
    
    print("YES" if is_bipartite else "NO")
