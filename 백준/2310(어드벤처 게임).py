def dfs(index, money):
    if index == n:
        return True
    
    room = rooms[index]
    room_type, amount, *adj = room
    amount = int(amount)
    
    if room_type == "L":
        money = max(money, amount)
    elif room_type == "T":
        if money < amount:
            return False
        else:
            money = money - amount
    
    for i in adj:
        if i == 0:
            break
        if dfs(i-1, money):
            return True
    
    return False

            
while True:
    n = int(input())
    if n == 0:
        break
    
    rooms = [input().split() for _ in range(n)]
    
    if dfs(0, 0):
        print("Yes")
    else:
        print("No")