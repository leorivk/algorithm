import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
adj_list = [[] for _ in range(n)]
visited = [False] * n
result = False

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def dfs(node, depth):
    global result
    if depth == 4: # 깊이가 4에 도달하면 조건을 만족
        result = True
        return
    visited[node] = True
    for i in adj_list[node]:
        if not visited[i]:
            dfs(i, depth + 1)
            if result: # 이미 결과를 찾았으면 더 이상 탐색 X
                return
    visited[node] = False # 백트래킹

for i in range(n):
    if not visited[i]:
        dfs(i, 0) 

print(1 if result else 0)
