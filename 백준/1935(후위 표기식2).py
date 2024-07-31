n=int(input())
exp=list(input())
num=[int(input()) for i in range(n)]

stk=[]

for i in exp:
    if i.isalpha():
        stk.append(num[ord(i)-65])
    else:
        a = stk.pop()
        b = stk.pop()
        
        if i == "+":
            b += a
        elif i == "-":
            b -= a
        elif i == "*":
            b *= a
        else:
            b /= a
        
        stk.append(b)

print('%.2f' %stk[-1])