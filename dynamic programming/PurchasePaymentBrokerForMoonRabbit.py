import sys
input = sys.stdin.readline

n = int(input())

money = [1,2,5,7]

INF = (1e9)

dp = [INF]*(100001)
dp[0] = 0

for i in money:
    dp[i] = 1

for i in range(1,n+1):
    for j in money:
        if i-j>=0:
            dp[i] = min(dp[i-j]+1,dp[i])

print(dp[n])