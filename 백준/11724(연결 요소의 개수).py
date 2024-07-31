import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(node):
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        # bfs(i)
        dfs(i)
        
        count += 1
        
print(count)
