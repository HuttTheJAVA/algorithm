import sys
import copy
input = sys.stdin.readline

dp = []
N,M = map(int,input().split())

for i in range(N):
    info = list(map(int,input().split()))
    dp.append(info)

n_lst = copy.deepcopy(dp)
    
for i in range(N):
    for j in range(M):
        if i-1>=0:
            dp[i][j] = max(dp[i-1][j]+n_lst[i][j],dp[i][j])
        if j-1>=0:
            dp[i][j] = max(dp[i][j-1]+n_lst[i][j],dp[i][j])

print(dp[N-1][M-1])