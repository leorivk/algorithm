from collections import deque

def solution(n, wires):
    def bfs(start, cut):
        visited = [False] * (n + 1)
        q = deque([start])
        visited[start] = True
        cnt = 1
        
        while q:
            cur = q.popleft()
            for adj in graph[cur]:
                if adj != cut and not visited[adj]:
                    q.append(adj)
                    visited[adj] = True
                    cnt += 1
        
        return cnt

    answer = n
    graph = [[] for _ in range(n + 1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        cnt1 = bfs(v1, v2)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1 - cnt2))
    
    return answer