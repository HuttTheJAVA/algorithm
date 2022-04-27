import sys
input = sys.stdin.readline

n = int(input())

data = []
dp = [[0]*n for i in range(n)]
for i in range(n):
    data.append(list(map(int,input().split())))

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0:
            if i == n-1 and j == n-1:
                continue
            if i+data[i][j]<n:
                dp[i+data[i][j]][j] += dp[i][j]
            if j+data[i][j]<n:
                dp[i][j+data[i][j]] += dp[i][j]

print(dp[n-1][n-1])