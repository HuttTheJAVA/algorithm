from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

commands = ["push","front","back","size","empty","pop"]

qu = deque()

for i in range(n):
    do = input().split()
    for i in range(len(commands)):
        if do[0] == commands[i]:
            if i == 0:
                qu.append(do[1])
            elif i == 1:
                if qu:
                    print(qu[0])
                else:
                    print(-1)
            elif i == 2:
                if qu:
                    print(qu[-1])
                else:
                    print(-1)
            elif i == 3:
                print(len(qu))
            elif i == 4:
                if qu:
                    print(0)
                else:
                    print(1)
            elif i == 5:
                if qu:
                    print(qu.popleft())
                else:
                    print(-1)