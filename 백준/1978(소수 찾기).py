def is_prime(n):
    if n < 2 : 
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0: 
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in nums:
    if is_prime(i):
        cnt += 1

print(cnt)