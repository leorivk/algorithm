from collections import deque

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n + 1):
    adj[i].sort()


def dfs(v):
    visited = [False] * (n + 1)
    stack = [v]
    result = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            for i in reversed(adj[node]):
                if not visited[i]:
                    stack.append(i)
    return result


def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    result = []
    visited[v] = True
    while queue:
        node = queue.popleft()
        result.append(node)
        for i in adj[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result


dfs_result = dfs(v)
bfs_result = bfs(v)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
