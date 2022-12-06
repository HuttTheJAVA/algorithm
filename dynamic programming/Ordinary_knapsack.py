import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0]*(k+1) for i in range(n+1)]

for th in range(1,n+1):
    T,I = map(int,input().split())
    for i in range(1,k+1):
        dp[th][i] = max(dp[th][i],dp[th-1][i],dp[th][i-1])
        if i >= T:
            dp[th][i] = max(dp[th][i],dp[th-1][i-T]+I)

print(dp[n][k])