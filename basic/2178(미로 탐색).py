from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, list(input()))) for _ in range(n)]

def bfs():
    q = deque()
    q.append([0, 0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append([nx, ny])

bfs()
print(maze[n-1][m-1])
                
        