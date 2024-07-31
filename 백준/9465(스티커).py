cnt = int(input())

for _ in range(cnt):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    d = [[0] * n for _ in range(2)]
    
    d[0][0] = sticker[0][0]
    d[1][0] = sticker[1][0]
    
    if n == 1:
        print(max(d[0][0], d[1][0]))
        continue

    d[0][1] = sticker[1][0] + sticker[0][1]
    d[1][1] = sticker[0][0] + sticker[1][1]
    if n == 2:
        print(max(d[0][1], d[1][1]))
        continue
    
    for i in range(2, n):
        d[0][i] = max(d[1][i - 1], d[1][i - 2]) + sticker[0][i]
        d[1][i] = max(d[0][i - 1], d[0][i - 2]) + sticker[1][i]

    print(max(d[0][-1], d[1][-1]))