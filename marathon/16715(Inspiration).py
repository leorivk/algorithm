def sum_digits(n, base):
    total_sum = 0
    while n > 0:
        total_sum += n % base
        n //= base
    return total_sum

n = int(input())

res_idx = 0
res_sum = 0
for i in range(2, n+1):
    cur_sum = sum_digits(n, i)
    if cur_sum > res_sum:
        res_sum = cur_sum
        res_idx = i

print(res_sum, res_idx)
