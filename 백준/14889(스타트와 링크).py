n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float("inf")

def calc_diff(team, n):
    team1 = set(team)
    team2 = set(range(n)) - team1
    
    ab1 = sum(s[i][j] for i in team1 for j in team1)
    ab2 = sum(s[i][j] for i in team2 for j in team2)
    
    return abs(ab1 - ab2)

def bt(i, team):
    global min_diff
    
    if len(team) == n//2:
        diff = calc_diff(team, n)
        min_diff = min(min_diff, diff)
        return
    
    if i == n:
        return
    
    bt(i + 1, team + [i])
    bt(i + 1, team)

bt(0, [])  
print(min_diff)