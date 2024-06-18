import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.read

data = input().split()
n = int(data[0])
m = int(data[1])
field = []
index = 2

for i in range(m):
    field.append(list(data[index + i]))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, color):
    cnt = 1
    field[x][y] = 'X'  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == color:
            cnt += dfs(nx, ny, color)
    return cnt

w_power = 0
b_power = 0

for i in range(m):
    for j in range(n):
        if field[i][j] == 'W':
            w_power += dfs(i, j, 'W') ** 2
        elif field[i][j] == 'B':
            b_power += dfs(i, j, 'B') ** 2

print(w_power, b_power)
