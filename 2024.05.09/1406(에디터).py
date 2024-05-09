import sys
input = sys.stdin.readline

stk = list(input().rstrip())
temp = []

for _ in range(int(input())):
    comm = list(input().split())
    if comm[0] == 'L':
        if stk:
            temp.append(stk.pop())    
    elif comm[0] == 'D':
    	if temp:
            stk.append(temp.pop())
    elif comm[0] == 'B':
        if stk:
            stk.pop()
    else:
        stk.append(comm[1])
        
stk.extend(reversed(temp))
print(''.join(stk))


        