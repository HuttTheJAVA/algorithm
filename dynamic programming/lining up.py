import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dp = [1]*(n+1)

show = [0]*(n+1)

lst = list(map(int,input().split()))

max_val = 1

for i in range(len(lst)):
    if show[lst[i]-1]:
        dp[lst[i]] += dp[lst[i]-1]
        max_val = max(max_val,dp[lst[i]])
    show[lst[i]] = 1


print(n-max_val)