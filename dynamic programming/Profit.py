import sys
from collections import deque

input = sys.stdin.readline

while(1):
    n = int(input())
    if not n:
        break
    n_lst = []
    for i in range(n):
        n_lst.append(int(input()))
    for i in range(1,n):
        if n_lst[i]+n_lst[i-1]>n_lst[i]:
            n_lst[i] = n_lst[i]+n_lst[i-1]
    print(max(n_lst))