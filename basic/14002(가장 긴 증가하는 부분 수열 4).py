n = int(input())
arr = list(map(int, input().split()))
d = [[] for _ in range(n)] 
d[0] = [arr[0]] 

for i in range(1, n):
    d[i] = [arr[i]] 
    for j in range(i):
        if arr[i] > arr[j] and len(d[i]) < len(d[j]) + 1:
            d[i] = d[j] + [arr[i]]  # 이전 부분 수열에 현재 요소 추가

max_length = max(len(seq) for seq in d)
max_sequence = max((seq for seq in d if len(seq) == max_length), key=lambda x: x[-1])

print(max_length)
print(*max_sequence)
