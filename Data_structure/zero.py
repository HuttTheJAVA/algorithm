import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
n_lst = []

for i in range(n):
    num = int(input())
    if num == 0:
        n_lst.pop()
    else:
        n_lst.append(num)

print(sum(n_lst))