import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

dp = [0]*(1000001)

end = max(n_lst)

for i in range(n):
    if n_lst[i]-1>=0 and dp[n_lst[i]-1]:
        dp[n_lst[i]] = dp[n_lst[i]-1]+1
    else:
        dp[n_lst[i]] = 1

print(max(dp))