import sys

n = int(sys.stdin.readline())

queue = []

for _ in range(n):
    comm = list(sys.stdin.readline().split())
    
    if comm[0] == "push":
        queue.append(comm[1])
    elif comm[0] == "pop":
        print(queue.pop(0) if queue else -1)
    elif comm[0] == "size":
        print(len(queue))
    elif comm[0] == "empty":
        print(0 if queue else 1)
    elif comm[0] == "front":
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)