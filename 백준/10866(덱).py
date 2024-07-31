# 스택 2개로 구현 (deque X)

import sys
input = sys.stdin.readline

n = int(input())
front = []
back = []

for _ in range(n):
    comm = list(input().split())
    if comm[0] == "push_front":
        front.append(comm[1])
    elif comm[0] == "push_back":
        back.append(comm[1])
    elif comm[0] == "pop_front":
        if not front:
            if not back:
                print(-1)
            else:
                while back:
                    front.append(back.pop())
                print(front.pop())
        else:
            print(front.pop())
    elif comm[0] == "pop_back":
        if not back:
            if not front:
                print(-1)
            else:
                while front:
                    back.append(front.pop())
                print(back.pop())
        else:
            print(back.pop())
    elif comm[0] == "size":
        print(len(front) + len(back))
    elif comm[0] == "empty":
        print(1 if not front and not back else 0)
    elif comm[0] == "front":
        if not front:
            if not back:
                print(-1)
            else:
                print(back[0])
        else:
            print(front[-1])
    else:
        if not back:
            if not front:
                print(-1)
            else:
                print(front[0])
        else:
            print(back[-1])