n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

def bt(flowers, total_cost):
    global min_cost
    if total_cost >= min_cost:
        return
    
    if len(flowers) == 15:  
        min_cost = min(min_cost, total_cost)
        return
    
    for x in range(1, n-1):
        for y in range(1, n-1):
            if all((x + dx[i], y + dy[i]) not in flowers for i in range(5)):
                temp = [(x + dx[i], y + dy[i]) for i in range(5)]
                cost = sum(garden[nx][ny] for nx, ny in temp)
                
                flowers.extend(temp)
                bt(flowers, total_cost + cost)
                for _ in range(5):
                    flowers.pop()

min_cost = float('inf')
bt([], 0)
print(min_cost)