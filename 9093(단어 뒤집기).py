n = int(input())

for _ in range(n):
    sentence = input().split()
    
    temp = []
    for i in sentence:
        temp.append(i[::-1])
    print(*temp)    
