from collections import deque

def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny] == 1:
                    cheese[nx][ny] = 0
                    count += 1
                else:
                    queue.append((nx, ny))
                visited[nx][ny] = True
    
    return count

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

time = 0
last_count = 0

while True:
    count = bfs()
    if count == 0:
        break
    last_count = count
    time += 1

print(time)
print(last_count)