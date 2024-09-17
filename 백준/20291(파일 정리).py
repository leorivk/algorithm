n = int(input())

dict = {}

for _ in range(n):
    file = input().split('.')
    ext = file[1]
    if ext in dict:
        dict[ext] += 1
    else:
        dict[ext] = 1

for ext in sorted(dict.keys()):
    print(f"{ext} {dict[ext]}")
