def is_balanced(string):
    stack = []
    brackets = {')': '(', ']': '['}
    for char in string:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()
            
    return len(stack) == 0

while True:
    string = input()
    if string == ".":
        break
    
    print("yes" if is_balanced(string) else "no")
        
    