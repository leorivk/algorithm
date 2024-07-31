him = input().strip()
her = input().strip()
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

# dp 리스트 초기화
dp = [[] for _ in range(2 * len(him) - 1)]

for i in range(len(him)):
    dp[0].append(alpha[ord(him[i]) - 65])
    dp[0].append(alpha[ord(her[i]) - 65])

# 각 단계별로 dp 리스트를 갱신
for i in range(1, len(dp)):
    for j in range(len(dp[i-1]) - 1):
        if len(dp[i]) <= j:
            dp[i].append(0)
        dp[i][j] = (dp[i-1][j] + dp[i-1][j + 1]) % 10

# 최종 결과 출력
print(dp[-1][0], dp[-1][1], sep='')
