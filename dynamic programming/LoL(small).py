import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dp = [0]*(n+1)
dp[0] = 1
skill = [1,m]

for i in range(1,n+1):
    for j in skill:
        if i-j >= 0:
            dp[i] += dp[i-j]

print(dp[n]%1000000007)