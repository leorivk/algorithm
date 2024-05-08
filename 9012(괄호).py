n = int(input())

for _ in range(n):
    pstr = input()
    stack = []
    
    is_correct = True
    for i in pstr:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                is_correct = False
                break
        
    if stack:
        is_correct = False
    
    print("YES" if is_correct else "NO")
    
    
    