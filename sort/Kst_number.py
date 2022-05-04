import sys
input = sys.stdin.readline

n,k = map(int,input().split())

n_lst = list(map(int,input().split()))

n_lst.sort()

print(n_lst[k-1])