import sys
input = sys.stdin.readline

INF = (1e9)

n,m = map(int,input().split())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

dp = [[INF]*m for i in range(n)]

dp[0][0] = 0

for i in range(n):
    for j in range(m):
        if dp[i][j] != INF:
            for k in range(1,data[i][j]+1):
                if 0<=i+k<n:
                    dp[i+k][j] = min(dp[i+k][j],dp[i][j]+1)
                if 0<=j+k<m:
                    dp[i][j+k] = min(dp[i][j+k],dp[i][j]+1)

print(dp[n-1][m-1])