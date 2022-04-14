from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

n_lst = []

for i in range(n):
    n_lst.append(int(input()))

n_lst.sort()

dissatic = 0

for i in range(n):
    dissatic += abs(n_lst[i]-(i+1))

print(dissatic)