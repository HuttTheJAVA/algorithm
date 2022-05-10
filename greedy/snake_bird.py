import sys
input = sys.stdin.readline

n,l = map(int,input().split())

n_lst = list(map(int,input().split()))

n_lst.sort()

for i in range(n):
    if n_lst[i]<=l:
        l += 1

print(l)