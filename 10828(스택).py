import sys

n = int(sys.stdin.readline())

stk = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push":
        stk.append(cmd[1])
    elif cmd[0] == "top":
        print(stk[-1] if stk else -1)
    elif cmd[0] == "size":
        print(len(stk))
    elif cmd[0] == "empty":
        print(0 if stk else 1)
    else:
        print(stk.pop() if stk else -1)


