from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,list(input().strip()))))

dp = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        dp[i][j] = matrix[i][j]
        if 0<=i-1<n:
            dp[i][j] += dp[i-1][j]
        if 0<=j-1<m:
            dp[i][j] += dp[i][j-1]
        if 0<=i-1<n and 0<=j-1<m:
            dp[i][j] -= dp[i-1][j-1]

max_score = 0

for i in range(n):
    for j in range(m):
        one_square_sum = dp[i][j]
        if i == n-1 and j == m-1:
            continue
        if j == m-1:
            for idx in range(i+1,n-1):  ## Case1
                two_square_sum = dp[idx][j] - dp[i][j]
                three_square_sum = dp[-1][j]-dp[idx][j]
                max_score = max(max_score,one_square_sum*two_square_sum*three_square_sum)
            
            for jdx in range(m-1):
                two_square_sum = dp[-1][jdx] - dp[i][jdx]
                three_square_sum = dp[-1][-1] - two_square_sum - dp[i][-1]
                max_score = max(max_score,one_square_sum*two_square_sum*three_square_sum)
        elif i == n-1:
            for jdx in range(j+1,m-1):
                two_square_sum = dp[i][jdx] - dp[i][j]
                three_square_sum = dp[i][-1] - dp[i][jdx]
                max_score = max(max_score,one_square_sum*two_square_sum*three_square_sum)
            
            for idx in range(n-1):
                two_square_sum = dp[idx][-1] - dp[idx][j]
                three_square_sum = dp[-1][-1] - two_square_sum - dp[i][j]
                max_score = max(max_score,one_square_sum*two_square_sum*three_square_sum)
        else:
            #### case 우측 끝단에 맞춘경우
            two_square_sum = dp[i][-1] - dp[i][j]
            three_square_sum = dp[-1][-1] - dp[i][-1]
            max_score = max(max_score,one_square_sum*two_square_sum*three_square_sum)
            #### case 아래 끝단에 맞춘경우
            two_square_sum = dp[-1][j] - dp[i][j]
            three_square_sum = dp[-1][-1] - dp[-1][j]
            max_score = max(max_score,one_square_sum*two_square_sum*three_square_sum)

print(max_score)