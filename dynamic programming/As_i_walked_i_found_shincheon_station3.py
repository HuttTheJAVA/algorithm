import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dp = [0]*10

dp[1] = 0
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1]*3

print(dp[n])