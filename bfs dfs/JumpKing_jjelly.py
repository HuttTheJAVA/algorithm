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
        if dp[i][j] == 1:
            if 0<=i+data[i][j]<n:
                dp[i+data[i][j]][j] = 1
            if 0<=j+data[i][j]<n:
                dp[i][j+data[i][j]] = 1

if dp[n-1][n-1] == 0:
    print("Hing")
else:
    print("HaruHaru")