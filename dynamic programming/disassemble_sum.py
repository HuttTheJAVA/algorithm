import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = [[0]*201 for i in range(201)]

for i in range(n+1):
    dp[1][i] = 1

for i in range(2,k+1):
    for j in range(n+1):
        dp[i][j] = sum(dp[i-1][:j+1])

print(dp[k][n]%1000000000)