import sys
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)][::-1]
snums = sorted(nums)

stack = []
temp = []
for num in snums:
    temp.append('+')
    stack.append(num)
    while stack and stack[-1] == nums[-1]:
        temp.append('-')
        stack.pop()
        nums.pop()

if stack:
    print("NO")
else:
    for i in temp:
        print(i)
