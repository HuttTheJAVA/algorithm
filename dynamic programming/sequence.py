import sys
from collections import deque

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

dp = [1]*(100001)
r_dp = [1]*(100001)

for i in range(1,n):
    if n_lst[i]>=n_lst[i-1]:
        dp[i] = max(dp[i],dp[i-1]+1)

n_lst = n_lst[::-1]

for j in range(1,n):
    if n_lst[j]>=n_lst[j-1]:
        r_dp[j] = max(r_dp[j],r_dp[j-1]+1)

if max(dp)>=max(r_dp):
    print(max(dp))
else:
    print(max(r_dp))