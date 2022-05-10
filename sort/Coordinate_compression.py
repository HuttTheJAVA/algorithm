import sys

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

n_lst_set = set(n_lst)

n_lst_set = list(n_lst_set)

n_lst_set.sort()

n_dict = {}

for i in range(len(n_lst_set)):
    n_dict[n_lst_set[i]] = i

for i in n_lst:
    print(n_dict[i],end=" ")