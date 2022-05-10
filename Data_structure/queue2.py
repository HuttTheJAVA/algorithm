from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

n_lst = deque()

for i in range(n):
    word = input().split()
    a = word[0] 
    if a == 'push':
        n_lst.append(word[1])

    elif a == 'pop':
        if n_lst:
            num = n_lst.popleft()
            print(num)
        else:
            print(-1)
    elif a == 'size':
        print(len(n_lst))

    elif a == 'empty':
        if n_lst:
            print(0)
        else:
            print(1)

    elif a == 'front':
        if n_lst:
            print(n_lst[0])
        else:
            print(-1)
        
    elif a == 'back':
        if n_lst:
            print(n_lst[-1])
        else:
            print(-1)
