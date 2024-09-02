from collections import deque

def bfs(n, k):
    queue = deque([n])
    visited = [-1] * 100001
    visited[n] = 0

    while queue:
        current = queue.popleft()
        if current == k:
            return visited[current]
        
        for next in (current - 1, current + 1, current * 2):
            if 0 <= next <= 100000 and visited[next] == -1:
                queue.append(next)
                visited[next] = visited[current] + 1

n, k = map(int, input().split())
print(bfs(n, k))