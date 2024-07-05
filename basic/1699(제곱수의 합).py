n = int(input())

d = [0] * (n+1) 

d[1] = 1
if n > 1:
    d[2] = 2
if n > 2:
    d[3] = 3

for i in range(4, n+1):
    if i ** 0.5 == 0:
        d[i] = 1
    else:
        d[i] = i  
        for j in range(1, int(i**0.5) + 1):
            d[i] = min(d[i], d[i - j*j] + 1)

print(d[n])