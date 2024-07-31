import sys
input = sys.stdin.readline

s = list(input().rstrip()) 

result = []
temp = []

is_tag = False

while s:
    top = s.pop(0)
    if top == " " and not is_tag:
        while temp:
            result.append(temp.pop())
        result.append(top)
    
    # if로 한다면 공백인 경우가 else에서 한 번 더 처리
    elif top == '<':
        while temp:
            result.append(temp.pop())
        is_tag = True
        result.append(top)
    
    elif top == '>':
        result.append(top)
        is_tag = False
    
    elif is_tag:
        result.append(top)
    
    else:
        temp.append(top)

if not is_tag:
    while temp:
        result.append(temp.pop())

print("".join(result))
