import sys
input = sys.stdin.readline


n = int(input())

n_lst = list(map(int,input().split()))

dp = [0]*(n)

for i in range(n-2,-1,-1):
    dp[i] = dp[i+1] + n_lst[i+1]

hab = 0

for i in range(n):
    hab += dp[i]*n_lst[i]

print(hab%1000000007)