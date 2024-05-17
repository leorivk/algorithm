while True:
    result = [0, 0, 0, 0]
    try:
        s = input()
        for i in s:
            if i.islower():
                result[0] += 1
            elif i.isupper():
                result[1] += 1
            elif i.isdigit():
                result[2] += 1
            elif i.isspace():
                result[3] += 1
        print(*result)
    except EOFError:
        break
