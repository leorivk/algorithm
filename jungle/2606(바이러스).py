import sys
sys.setrecursionlimit(10 ** 6)

from collections import deque

computers = int(input())
links = int(input())

adj = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)
visited[1] = True

for _ in range(links):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
def bfs(adj, start):
    q = deque([start])
    
    cnt = 0
    while q:
        node = q.popleft()
        for i in adj[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

    return cnt
    
def dfs(node):
    visited[node] = True
    cnt = 1
    for i in adj[node]:
        if not visited[i]:
            cnt += dfs(i)
    return cnt

# print(bfs(adj, 1))
print(dfs(1) - 1)
