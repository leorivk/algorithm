def solution(seq, k):
    n = len(seq)
    right, left = 0, 0
    current_sum = 0
    min_length = n + 1 
    result = [0, n - 1]

    while left < n:
        current_sum += seq[left]
        
        while current_sum >= k:
            if current_sum == k:
                length = left - right + 1
                if length < min_length:
                    min_length = length
                    result = [right, left]
            
            current_sum -= seq[right]
            right += 1
        
        left += 1

    return result