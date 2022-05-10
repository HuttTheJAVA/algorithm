import sys
input = sys.stdin.readline

n,k = map(int,input().split())

dp = list(map(int,input().split()))

dp.sort()

exp = 0

for i in range(1,n):
    if i<k:
        exp += i*dp[i]
    else:
        exp += k*dp[i]

print(exp)