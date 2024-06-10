import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, visited, graph):
    visited[x][y] = True
    
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny, visited, graph)

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
        
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited, graph)
                cnt += 1
    print(cnt)
