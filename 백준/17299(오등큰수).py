n = int(input())
a = list(map(int, input().split()))[::-1]

f = {}
result = [-1] * n

for i in a:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

temp = []

for i in range(n):
    while temp:
        if f[a[i]] < f[temp[-1]]:
            result[i] = temp[-1]  
            break  
        temp.pop()  
    temp.append(a[i])  

print(*result[::-1])
