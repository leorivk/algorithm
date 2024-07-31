n = int(input())

test = [int(input()) for _ in range(n)]


def dp(x):
    if x <= 3:
        d = [0, 1, 2, 4]
        return d[x]
    else:
        d = [0] * (x + 1)
        d[1] = 1
        d[2] = 2
        d[3] = 4
        for i in range(4, x+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        return d[x]


for i in test:
    print(dp(i))