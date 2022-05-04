from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

lst = deque()

for i in range(n):
    command = input().split()
    if command[0] == 'push_front':
        lst.appendleft(command[1])
    elif command[0] == "push_back":
        lst.append(command[1])
    elif command[0] == "pop_front":
        if lst:
            print(lst.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(lst))
    elif command[0] == "empty":
        if lst:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif command[0] == "back":
        if lst:
            print(lst[-1])
        else:
            print(-1)
        