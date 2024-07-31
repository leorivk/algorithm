from collections import deque

n, k = map(int, input().split())

q = deque()
for i in range(1, n+1): q.append(i)
result = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print(str(result).replace('[', '<').replace(']', '>'))