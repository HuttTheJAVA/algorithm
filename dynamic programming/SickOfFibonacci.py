import sys

input = sys.stdin.readline

INF = (1e9)

n = int(input())

dp = [0]*51

dp[0] = 1
dp[1] = 1
def fibo(n):
    if n<2:
        return 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]+1
    return dp[n]

print(fibo(n)%1000000007)