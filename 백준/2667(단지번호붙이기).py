n = int(input())

vil = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    
    cnt = 1 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and vil[nx][ny] == '1' and not visited[nx][ny]:
            cnt += dfs(nx, ny) 
    
    return cnt

count = 0
houses = []
for i in range(n):
    for j in range(n):
        if vil[i][j] == '1' and not visited[i][j]:
            houses.append(dfs(i, j))

houses.sort()
print(len(houses))
for house in houses:
    print(house) 