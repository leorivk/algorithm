exp = input()

stk = []
answer = ""

hp = ["*", "/"]

for i in exp:
    if i == '(':
        stk.append(i)
        
    elif i == ')':
        while stk and stk[-1] != '(':
            answer += stk.pop()
        stk.pop()  # 여는 괄호 제거
        
    elif i.isalpha():
        answer += i
        
    elif i in hp:
        while stk and stk[-1] in hp:
            answer += stk.pop()
        stk.append(i)
        
    else: 
        while stk and stk[-1] != '(':
            answer += stk.pop()
        stk.append(i)
    
    print(stk)
    
while stk:
    answer += stk.pop()

print(answer)
