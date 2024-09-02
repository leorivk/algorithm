n = int(input())
students = n ** 2

liked = {}
classroom = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(students):
    numbers = list(map(int, input().split()))
    student = numbers[0]
    liked[student] = set(numbers[1:])
    
    max_liked = -1
    max_empty = -1
    cur = (-1, -1)
    for i in range(n):
        for j in range(n):
            if classroom[i][j] != 0:
                continue
            
            liked_cnt = 0
            empty_cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] in liked[student]:
                        liked_cnt += 1
                    elif classroom[nx][ny] == 0:
                        empty_cnt += 1
            
            if (liked_cnt, empty_cnt, -i, -j) > (max_liked, max_empty, cur[0], cur[1]):
                max_liked, max_empty = liked_cnt, empty_cnt
                cur = (i, j)
                    
    classroom[cur[0]][cur[1]] = student

satisfaction = 0
for i in range(n):
    for j in range(n):
        student = classroom[i][j]
        count = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n and classroom[nx][ny] in liked[student]:
                count += 1
        if count > 0:
            satisfaction += 10 ** (count - 1)

print(satisfaction)