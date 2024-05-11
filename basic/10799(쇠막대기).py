import sys

input = sys.stdin.readline

pieces = input().strip()  

stk = []

result = 0

for i in range(len(pieces)):
    if pieces[i] == '(':
        stk.append(i)  
    else:
        
        if pieces[i - 1] == '(':
            stk.pop()  
            result += len(stk)  
        else:
            stk.pop()  
            result += 1 

print(result)
