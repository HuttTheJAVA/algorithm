import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

bomb = []

go_right = [0]*n

go_left = [0]*n

for i in range(n):
    bomb.append(int(input()))

for i in range(n-1):
    if bomb[i] > bomb[i+1]:
        go_right[i+1] = 1

for i in range(n-1,0,-1):
    if bomb[i] > bomb[i-1]:
        go_left[i-1] = 1

order = []

for i in range(n):
    if not go_right[i] and not go_left[i]:
        order.append(i+1)

for i in order:
    print(i)