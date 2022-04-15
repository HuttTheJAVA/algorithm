import sys

input = sys.stdin.readline

n = int(input())

n_lst = []

max_weight = 0

for i in range(n):
    n_lst.append(int(input()))

n_lst.sort()

for i in range(n):
    max_weight = max(max_weight,(n-i)*n_lst[i])

print(max_weight)