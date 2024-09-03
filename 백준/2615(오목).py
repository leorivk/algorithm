import sys

board = [list(map(int, input().split())) for _ in range(19)]

directions = [(0, 1), (1, 0), (1, 1), (-1, 1)] 

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            color = board[x][y]

            for dx, dy in directions:
                cnt = 1
                nx, ny = x + dx, y + dy

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x - dx < 19 and 0 <= y - dy < 19 and board[x - dx][y - dy] == color:
                            break
                        if 0 <= nx + dx < 19 and 0 <= ny + dy < 19 and board[nx + dx][ny + dy] == color:
                            break
                        
                        print(color)
                        print(x + 1, y + 1)
                        
                        sys.exit(0)

                    nx, ny = nx + dx, ny + dy

print(0)