import sys

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

dp = [1]*(1001)

for i in range(n):
    for j in range(i):
        if n_lst[i]>n_lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))