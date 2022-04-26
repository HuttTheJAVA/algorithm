import sys
import math as m

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

for i in range(1,len(n_lst)):
    g = m.gcd(n_lst[0],n_lst[i])
    print("%d/%d"%((n_lst[0]//g),(n_lst[i]//g)))