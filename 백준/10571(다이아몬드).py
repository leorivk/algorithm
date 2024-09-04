t = int(input())

for _ in range(t):
    n = int(input())
    diamonds = []
    for _ in range(n):
        w, v = map(float, input().split())
        diamonds.append((w, v))
    
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if diamonds[i][0] > diamonds[j][0] and diamonds[i][1] < diamonds[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))