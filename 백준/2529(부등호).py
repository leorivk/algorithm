k = int(input())
signs = input().split()
max_num, min_num = "", ""
used = [False] * 10

def bt(stack):
    global max_num, min_num
    
    if len(stack) == k + 1:
        num = ''.join(map(str, stack))
        if not min_num:
            min_num = num
        max_num = num
        return
    
    for i in range(10):
        if used[i]:
            continue
        if len(stack) == 0 or (signs[len(stack)-1] == '<' and stack[-1] < i) or (signs[len(stack)-1] == '>' and stack[-1] > i):
            used[i] = True
            stack.append(i)
            bt(stack)
            stack.pop()
            used[i] = False

bt([])
print(max_num)
print(min_num)