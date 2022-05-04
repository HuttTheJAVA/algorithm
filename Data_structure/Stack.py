import sys
from collections import deque

input = sys.stdin.readline


lst = deque()

def push(n):
    lst.append(n)

def pop():
    if len(lst):
        num = lst.pop()
        print(num)
    else:
        print(-1)

def size():
    print(len(lst))

def empty():
    if len(lst)==0:
        print(1)
    else:
        print(0)

def top():
    if len(lst):
        print(lst[-1])
    else:
        print(-1)

n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == "top":
        top()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'pop':
        pop()