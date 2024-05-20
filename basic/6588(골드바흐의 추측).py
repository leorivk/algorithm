import sys
input = sys.stdin.readline

def sieve(n):
    arr = [True] * (n + 1)
    arr[0], arr[1] = False, False
    
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    
    return [i for i in range(n + 1) if arr[i]]

# 소수를 미리 계산하여 저장
primes = sieve(1000000)
primes_set = set(primes)



while True:
    n = int(input().strip())
    if n == 0:
        break
    
    found = False
    for p in primes:
        if p > n:
            break
        if (n - p) in primes_set:
            print(f"{n} = {p} + {n - p}")
            found = True
            break
    
    if not found:
        print("Goldbach's conjecture is wrong.")

print(len(primes))
print(len(set(primes)))