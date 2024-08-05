from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

num = 2
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            q = deque([(i, j)])
            grid[i][j] = num
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = num
                        q.append((nx, ny))
            num += 1

q = deque()
dist = [[-1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] > 1:
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    q.append((i, j))
                    dist[i][j] = 0
                    break

result = float('inf')

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                grid[nx][ny] = grid[x][y]
                q.append((nx, ny))
            elif grid[nx][ny] != grid[x][y]:
                result = min(result, dist[x][y] + dist[nx][ny])

print(result)