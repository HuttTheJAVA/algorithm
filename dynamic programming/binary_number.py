import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dp = [0]*1001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4,n+1):
    if i%2 == 0:
        dp[i] = sum(dp[:i])+1
    else:
        dp[i] = sum(dp[:i])

print(dp[n])