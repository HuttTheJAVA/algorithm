import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

hab = n_lst.pop(n_lst.index(max(n_lst)))

hab += sum(n_lst)/2

if int(hab) == hab:
    print(int(hab))
else:
    print(hab)