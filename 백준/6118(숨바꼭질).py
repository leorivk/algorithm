from collections import deque

n, m = map(int, input().split())

adj = {i: [] for i in range(1, n+1)}  

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a) 

def bfs():
    q = deque([(1, 0)]) 
    visited = [False] * (n+1)
    visited[1] = True
    
    max_d = 0
    max_n = []
    
    while q:
        node, dist = q.popleft()
        
        if dist > max_d:
            max_d = dist
            max_n = [node]
        elif dist == max_d:
            max_n.append(node)
        
        for i in adj[node]:
            if not visited[i]:
                q.append([i, dist+1])
                visited[i] = True
    
    return min(max_n), max_d, len(max_n)

node, dist, cnt = bfs()

print(node, dist, cnt)