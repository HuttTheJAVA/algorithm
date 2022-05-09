from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

max_val = n_lst.pop(n_lst.index(max(n_lst)))

print(max_val*len(n_lst)+sum(n_lst))