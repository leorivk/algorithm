n, p, q = map(int, input().split())

dp = {0: 1} 

def sol(i):
    if i not in dp:
        dp[i] = sol(i // p) + sol(i // q)
    return dp[i]

print(sol(n))
