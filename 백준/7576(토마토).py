from collections import deque

m, n = map(int, input().split())  # m과 n의 순서를 바꿨습니다

tmt = [list(map(int, input().split())) for _ in range(n)]

q = deque([(i, j) for i in range(n) for j in range(m) if tmt[i][j] == 1])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tmt[nx][ny] == 0:
            tmt[nx][ny] = tmt[x][y] + 1
            q.append((nx, ny))  
    
# for row in tmt:
#     if 0 in row:
#         print(-1)
#         exit()

# print(max(max(row) for row in tmt) - 1)

if any(0 in row for row in tmt):  # 더 효율적인 검사 방법
    print(-1)
else:
    print(max(max(row) for row in tmt) - 1)
    