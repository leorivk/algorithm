from collections import deque

for _ in range(int(input())):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n + 2)]
    start, *stores, end = points
    
    q = deque([start])
    visited = set([start])
    success = False
    
    while q:
        x, y = q.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            success = True
            break
        
        for nx, ny in stores:
            if (nx, ny) not in visited and abs(x - nx) + abs(y - ny) <= 1000:
                q.append((nx, ny))
                visited.add((nx, ny))
    
    print("happy" if success else "sad")