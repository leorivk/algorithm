n = input()
result = [0]*26

for i in n:
    result[ord(i)-97] += 1
    
print(*result)