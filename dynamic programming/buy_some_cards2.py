import sys

INF = (1e9)
input = sys.stdin.readline

n = int(input())

dp = [INF]*1001

n_lst = [0]

n_lst = n_lst+list(map(int,input().split()))

for i in range(1,1001):
    if i < len(n_lst):
        dp[i] = n_lst[i]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i-j>=0:
            dp[i] = min(dp[i],dp[i-j]+n_lst[j])

print(dp[n])