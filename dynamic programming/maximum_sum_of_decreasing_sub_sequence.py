import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

dp = [0]*1000

n_lst = list(map(int,input().split()))

n_lst = n_lst[::-1]

for i in range(n):
    dp[i] = n_lst[i]

for i in range(n):
    for j in range(i):
        if n_lst[i]>n_lst[j]:
            dp[i] = max(dp[i],n_lst[i]+dp[j])

print(max(dp))