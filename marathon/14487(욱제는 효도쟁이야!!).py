n = int(input()) 
cost = list(map(int, input().split()))

print(sum(cost) - max(cost))