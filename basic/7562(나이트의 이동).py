from collections import deque

case = int(input())

def bfs(n, start_x, start_y, end_x, end_y):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    board = [[-1] * n for _ in range(n)]
    
    q = deque()
    q.append((start_x, start_y))
    
    board[start_x][start_y] = 0
    
    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return board[x][y]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    
    return -1
            
for _ in range(case):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
 
    print(bfs(n, start_x, start_y, end_x, end_y))

            
        
        