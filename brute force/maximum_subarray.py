import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    amount = int(input())
    n_lst = list(map(int,input().split()))
    for j in range(1,len(n_lst)):
        n_lst[j] = max(n_lst[j],n_lst[j]+n_lst[j-1])

    print(max(n_lst))