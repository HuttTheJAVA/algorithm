import sys
input = sys.stdin.readline

n,m = map(int,input().split())

n_lst = list(map(int,input().split()))

n_lst.sort()

for i in range(m):
    n_lst[0],n_lst[1] = n_lst[0]+n_lst[1],n_lst[0]+n_lst[1]
    n_lst.sort()

print(sum(n_lst))