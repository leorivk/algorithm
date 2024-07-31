def dfs(x, y, start_x, start_y, color, length):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == color:
            if (nx, ny) == (start_x, start_y) and length >= 3:
                return True
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny, start_x, start_y, color, length + 1):
                    return True
                visited[nx][ny] = False
    return False

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        if dfs(i, j, i, j, board[i][j], 1):
            print('Yes')
            exit()
        visited[i][j] = False

print('No')