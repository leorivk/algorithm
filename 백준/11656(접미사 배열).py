s = input()

result = []

for i in range(len(s)):
    result.append(s[i:])

for i in sorted(result):
    print(i)