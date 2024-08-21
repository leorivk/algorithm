from collections import deque

def bfs(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([(x, y)])  # 튜플로 좌표 추가
    rect[x][y] = 1
    cnt = 1  
    
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and rect[nx][ny] == 0:
                rect[nx][ny] = 1  
                q.append((nx, ny))  
                cnt += 1
    
    return cnt

m, n, k = map(int, input().split())

rect = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2): 
            rect[j][i] = 1

area = []

for i in range(m):
    for j in range(n):
        if rect[i][j] == 0:
            area.append(bfs(i, j))

area.sort()
print(len(area)) 
print(*area)  