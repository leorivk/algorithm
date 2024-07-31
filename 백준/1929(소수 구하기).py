def prime(start, end):
    if start < 2:
        start = 2
    
    arr = [True] * (end + 1)
    arr[0] = arr[1] = False 
    
    for i in range(2, int(end ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, end + 1, i):
                arr[j] = False
    
    return [i for i in range(start, end + 1) if arr[i]]

s, e = map(int, input().split())
print(*prime(s, e))

